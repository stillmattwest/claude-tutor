"""Layer 2 — run a scripted multi-turn tutor session in a sandbox and assert.

A scenario composes a throwaway repo (live `.claude/` + `CLAUDE.md` over a
fixture's student state), plays a fixed list of student turns through headless
`claude -p`, then runs the scenario's `check()` against the resulting files and
transcript.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import time
from collections.abc import Callable, Iterable
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from common import REPO_ROOT, Result, ScenarioReport

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
WORK_ROOT = Path(__file__).resolve().parent / ".work"

TURN_TIMEOUT_S = 480
DEFAULT_MODEL = "sonnet"
PER_TURN_BUDGET_USD = 2.5


@dataclass
class Transcript:
    turns: list[dict] = field(default_factory=list)

    def record(self, prompt: str, payload: dict) -> None:
        self.turns.append(
            {
                "prompt": prompt,
                "text": payload.get("result", "") or "",
                "cost": float(payload.get("total_cost_usd", 0) or 0),
                "is_error": bool(payload.get("is_error", False)),
                "session_id": payload.get("session_id", ""),
                "raw": payload,
            }
        )

    def turn(self, i: int) -> str:
        """1-indexed assistant text for turn i."""
        return self.turns[i - 1]["text"]

    @property
    def last(self) -> str:
        return self.turns[-1]["text"] if self.turns else ""

    @property
    def all_text(self) -> str:
        return "\n\n".join(t["text"] for t in self.turns)

    @property
    def total_cost(self) -> float:
        return sum(t["cost"] for t in self.turns)

    @property
    def had_error(self) -> bool:
        return any(t["is_error"] for t in self.turns)


CheckFn = Callable[[Path, Transcript], Iterable[Result]]


@dataclass
class Scenario:
    name: str
    fixture: str
    turns: list[str]
    check: CheckFn
    runs: int = 2
    need: int = 2
    fast: bool = False
    # 1-indexed turn -> {relative path: contents} written into the sandbox
    # just before that student turn runs (models "the student edited these files").
    write_before: dict[int, dict[str, str]] = field(default_factory=dict)


def compose_sandbox(fixture: str, dest: Path) -> Path:
    """Live skills + CLAUDE.md over the fixture's student state."""
    dest.mkdir(parents=True, exist_ok=True)
    shutil.copytree(REPO_ROOT / ".claude", dest / ".claude", dirs_exist_ok=True)
    for name in ("CLAUDE.md", "README.md"):
        shutil.copy2(REPO_ROOT / name, dest / name)
    for d in ("curriculum", "workspace", ".data"):
        (dest / d).mkdir(exist_ok=True)
    fixture_dir = FIXTURES_DIR / fixture
    if not fixture_dir.is_dir():
        raise FileNotFoundError(f"unknown fixture: {fixture}")
    shutil.copytree(fixture_dir, dest, dirs_exist_ok=True)
    return dest


def run_turn(workdir: Path, prompt: str, *, model: str, first: bool) -> dict:
    cmd = [
        "claude",
        "-p",
        prompt,
        "--output-format",
        "json",
        "--permission-mode",
        "bypassPermissions",
        "--setting-sources",
        "project",
        "--model",
        model,
        "--max-turns",
        "40",
        "--max-budget-usd",
        str(PER_TURN_BUDGET_USD),
    ]
    if not first:
        cmd.append("--continue")
    proc = subprocess.run(
        cmd,
        cwd=workdir,
        capture_output=True,
        text=True,
        timeout=TURN_TIMEOUT_S,
    )
    out = proc.stdout.strip()
    if not out:
        return {"is_error": True, "result": f"(no stdout; rc={proc.returncode}) {proc.stderr[:500]}"}
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        # stream-json or trailing noise: take the last JSON line
        for line in reversed(out.splitlines()):
            line = line.strip()
            if line.startswith("{"):
                try:
                    return json.loads(line)
                except json.JSONDecodeError:
                    continue
        return {"is_error": True, "result": f"(unparseable stdout) {out[:500]}"}


def _one_run(scenario: Scenario, model: str, work_root: Path, keep: bool) -> tuple[list[Result], float, str]:
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    sandbox = work_root / f"{scenario.name}-{stamp}"
    transcript = Transcript()

    def dump_transcript() -> None:
        try:
            (sandbox / "_transcript.json").write_text(
                json.dumps(transcript.turns, indent=2, default=str)
            )
        except OSError:
            pass

    try:
        compose_sandbox(scenario.fixture, sandbox)
        for idx, prompt in enumerate(scenario.turns):
            for rel, content in scenario.write_before.get(idx + 1, {}).items():
                dest = sandbox / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(content)
            payload = run_turn(sandbox, prompt, model=model, first=(idx == 0))
            transcript.record(prompt, payload)
        if transcript.had_error:
            dump_transcript()
            return [], transcript.total_cost, f"turn error: {transcript.last[:200]}"
        results = list(scenario.check(sandbox, transcript))
        if all(r.ok for r in results) and not keep:
            shutil.rmtree(sandbox, ignore_errors=True)
        else:
            dump_transcript()
        return results, transcript.total_cost, ""
    except subprocess.TimeoutExpired:
        dump_transcript()
        return [], transcript.total_cost, f"timeout after {TURN_TIMEOUT_S}s"
    except Exception as exc:  # noqa: BLE001 - surface any harness failure as a scenario error
        dump_transcript()
        return [], transcript.total_cost, f"{type(exc).__name__}: {exc}"


def run_scenario(
    scenario: Scenario,
    *,
    model: str = DEFAULT_MODEL,
    runs: int | None = None,
    keep: bool = False,
    work_root: Path = WORK_ROOT,
) -> ScenarioReport:
    total_runs = runs or scenario.runs
    work_root.mkdir(parents=True, exist_ok=True)
    report = ScenarioReport(
        name=scenario.name, runs=total_runs, need=min(scenario.need, total_runs),
        passed_runs=0,
    )
    harness_errors: list[str] = []
    for _ in range(total_runs):
        results, cost, error = _one_run(scenario, model, work_root, keep)
        report.cost_usd += cost
        if error:
            harness_errors.append(error)
            report.per_run.append([Result("run completed", False, error)])
            continue
        report.per_run.append(results)
        if all(r.ok for r in results):
            report.passed_runs += 1
    if len(harness_errors) == total_runs:
        # nothing actually exercised the assertions
        report.error = harness_errors[0]
    return report
