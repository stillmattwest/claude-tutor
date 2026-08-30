"""Assertion helpers for scenario `check()` functions.

File-state helpers read the sandbox after the run (robust). Text helpers match
against transcript turns. `judge()` delegates a fuzzy tone/pedagogy question to a
separate graded `claude -p` call.
"""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

from common import Result

JUDGE_MODEL = "sonnet"
JUDGE_SCHEMA = {
    "type": "object",
    "properties": {
        "score": {"type": "integer", "minimum": 1, "maximum": 5},
        "pass": {"type": "boolean"},
        "reason": {"type": "string"},
    },
    "required": ["score", "pass", "reason"],
    "additionalProperties": False,
}


def _read(path: Path) -> str:
    try:
        return path.read_text()
    except (FileNotFoundError, IsADirectoryError, UnicodeDecodeError):
        return ""


def file_exists(path: Path, label: str | None = None) -> Result:
    return Result(label or f"exists: {path.name}", path.exists())


def file_absent(path: Path, label: str | None = None) -> Result:
    return Result(label or f"absent: {path.name}", not path.exists())


def glob_exists(root: Path, pattern: str, label: str | None = None) -> Result:
    hits = list(root.glob(pattern))
    return Result(label or f"matches {pattern}", bool(hits), hits[0].name if hits else "none found")


def file_matches(path: Path, pattern: str, label: str) -> Result:
    text = _read(path)
    ok = re.search(pattern, text, re.MULTILINE) is not None
    detail = "" if ok else (f"{path.name} missing /{pattern}/" if text else f"{path.name} not found")
    return Result(label, ok, detail)


def file_lacks(path: Path, pattern: str, label: str) -> Result:
    text = _read(path)
    m = re.search(pattern, text, re.MULTILINE)
    return Result(label, m is None, "" if m is None else f"found /{pattern}/ in {path.name}")


def file_unchanged(path: Path, baseline: str, label: str) -> Result:
    return Result(label, _read(path) == baseline, "" if _read(path) == baseline else "file was modified")


def text_has(sample: str, pattern: str, label: str) -> Result:
    ok = re.search(pattern, sample, re.IGNORECASE | re.MULTILINE) is not None
    return Result(label, ok, "" if ok else f"no match for /{pattern}/")


def text_lacks(sample: str, pattern: str, label: str) -> Result:
    m = re.search(pattern, sample, re.IGNORECASE | re.MULTILINE)
    return Result(label, m is None, "" if m is None else f"unexpected match for /{pattern}/")


def count_questions(sample: str) -> int:
    """Rough count of question sentences in a chat message."""
    return len(re.findall(r"\?(\s|$)", sample))


def judge(rubric: str, sample: str, *, threshold: int = 4, label: str = "judge", model: str = JUDGE_MODEL) -> Result:
    prompt = (
        "You are grading one message from a coding tutor against a rubric. "
        "Score 1-5 how well it satisfies ALL rubric points, set pass=(score>="
        f"{threshold}), and give a one-sentence reason.\n\n"
        f"RUBRIC:\n{rubric}\n\nMESSAGE:\n{sample}\n"
    )
    try:
        proc = subprocess.run(
            [
                "claude", "-p", prompt,
                "--output-format", "json",
                "--model", model,
                "--permission-mode", "bypassPermissions",
                "--json-schema", json.dumps(JUDGE_SCHEMA),
            ],
            capture_output=True, text=True, timeout=180,
        )
        payload = json.loads(proc.stdout.strip())
        raw = payload.get("result", payload)
        verdict = raw if isinstance(raw, dict) else json.loads(raw)
        ok = bool(verdict.get("pass"))
        return Result(label, ok, f"score {verdict.get('score')}: {verdict.get('reason', '')}")
    except Exception as exc:  # noqa: BLE001
        return Result(label, False, f"judge failed: {type(exc).__name__}: {exc}")
