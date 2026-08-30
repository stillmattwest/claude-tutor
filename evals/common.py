"""Shared types and helpers for the claude-tutor eval harness."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / ".claude" / "skills"


@dataclass
class Result:
    """One assertion outcome."""

    label: str
    ok: bool
    detail: str = ""

    def line(self) -> str:
        mark = "PASS" if self.ok else "FAIL"
        tail = f" — {self.detail}" if self.detail else ""
        return f"  [{mark}] {self.label}{tail}"


@dataclass
class ScenarioReport:
    name: str
    runs: int
    need: int
    passed_runs: int
    per_run: list[list[Result]] = field(default_factory=list)
    cost_usd: float = 0.0
    error: str = ""

    @property
    def ok(self) -> bool:
        return not self.error and self.passed_runs >= self.need


def skill_names() -> set[str]:
    """Directory names under .claude/skills/ — the canonical set of skills."""
    return {p.name for p in SKILLS_DIR.iterdir() if (p / "SKILL.md").exists()}


def iter_skill_docs():
    """Yield every .md file that lives inside a skill directory."""
    yield from sorted(SKILLS_DIR.glob("*/*.md"))


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Minimal `key: value` frontmatter parser. Returns (fields, body)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw = text[3:end].strip("\n")
    body = text[end + 4 :]
    fields: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields, body


def print_report(scenario_reports: list[ScenarioReport], lint_results: list[Result]) -> None:
    if lint_results:
        print("\n=== static lint ===")
        for r in lint_results:
            print(r.line())
    if scenario_reports:
        print("\n=== behavioural scenarios ===")
        width = max(len(s.name) for s in scenario_reports)
        for s in scenario_reports:
            verdict = "PASS" if s.ok else "FAIL"
            note = s.error or f"{s.passed_runs}/{s.runs} runs (need {s.need})"
            cost = f"  ${s.cost_usd:.2f}" if s.cost_usd else ""
            print(f"  [{verdict}] {s.name.ljust(width)}  {note}{cost}")
            if not s.ok and not s.error:
                for run in s.per_run:
                    for r in run:
                        if not r.ok:
                            print(f"          {r.line().strip()}")


_SLUG = re.compile(r"[^a-z0-9]+")


def slug(text: str) -> str:
    return _SLUG.sub("-", text.lower()).strip("-")
