"""Mastertrack scenarios: the course-end handoff, and review with no live course."""

from __future__ import annotations

from pathlib import Path

from assertions import (
    file_absent,
    file_lacks,
    file_matches,
    glob_exists,
    text_has,
    text_lacks,
)
from harness import Scenario, Transcript


def _handoff_check(w: Path, t: Transcript):
    yield file_matches(w / ".data" / "IN_MASTERTRACK_CURRICULUM", r"^\s*off", "flag flipped to off")
    yield glob_exists(w, "curriculum/tracks/*/CURRICULUM.md", "course archived under curriculum/tracks/")
    yield glob_exists(
        w, "curriculum/tracks/*/lessons/**/*.md", "saved lesson plans archived with the course"
    )
    yield file_absent(w / "curriculum" / "CURRICULUM.md", "live CURRICULUM.md removed from repo root")
    yield file_matches(
        w / "curriculum" / "MASTERTRACK.md",
        r"(?i)current item:.*(pause|not started|C2)",
        "map current item is paused / points at C2",
    )
    yield file_matches(
        w / ".data" / "MASTERTRACK.md",
        r"(?i)(current item|current item status).*(pause|C2|not started)",
        "progress file current item updated",
    )
    yield text_lacks(
        t.all_text,
        r"(?im)^#\s*current lesson:|let's (start|begin) (the next course|C2)|first lesson of postgres",
        "did not start the next course",
    )
    yield text_has(
        t.all_text,
        r"(?i)congrat|well done|nice work|great work|you.?ve (finished|completed|done)"
        r"|that.?s (the |your )?.{0,25}course (done|complete|finished|wrapped)"
        r"|milestone|take the win|real (checkpoint|accomplishment)|proud|first course",
        "celebrates finishing the course",
    )


def _review_noop_check(w: Path, t: Transcript):
    yield text_has(
        t.turn(1),
        r"(?i)nothing to review|no skills? (table|yet)|haven.?t started|once you.?ve (started|begun)"
        r"|not yet any|no lessons yet",
        "explains there is nothing to review yet",
    )
    yield file_lacks(w / ".data" / "STUDENT.md", r"(?m)^##\s*Skills", "did not invent a Skills table")
    yield file_absent(w / "curriculum" / "CURRICULUM.md", "did not write a curriculum")


SCENARIOS = [
    Scenario(
        name="mastertrack_course_end_handoff",
        fixture="mastertrack-course-end",
        write_before={
            1: {
                "workspace/greetings/core.py": (
                    'def greet(name):\n    if not name:\n        name = "there"\n'
                    '    return f"Hello, {name}!"\n'
                ),
                "workspace/tests/test_core.py": (
                    "from greetings.core import greet\n\n\n"
                    'def test_greet_uses_the_name():\n    assert greet("Devon") == "Hello, Devon!"\n\n\n'
                    'def test_greet_handles_empty_name():\n    assert greet("") == "Hello, there!"\n'
                ),
            }
        },
        turns=[
            "I updated greetings/core.py to fall back to 'there' for an empty name and "
            "added a second test in tests/test_core.py for the empty case. Both files "
            "are saved. `pytest` from inside workspace/ shows `2 passed`.",
            "Yes, 2 passed. I think that was the last lesson of the course?",
            "Great. Yes, please close out the course.",
        ],
        check=_handoff_check,
        runs=2,
        need=2,
        fast=True,
    ),
    Scenario(
        name="review_noop_without_skills_table",
        fixture="mastertrack-designed",
        turns=["/review"],
        check=_review_noop_check,
        runs=2,
        need=2,
    ),
]
