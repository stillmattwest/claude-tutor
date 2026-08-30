"""Curriculum-design and path-integrity scenarios."""

from __future__ import annotations

from pathlib import Path

from assertions import (
    file_absent,
    file_exists,
    file_matches,
    file_unchanged,
    judge,
    text_has,
    text_lacks,
)
from harness import FIXTURES_DIR, Scenario, Transcript


def _design_check(w: Path, t: Transcript):
    cur = w / "curriculum" / "CURRICULUM.md"
    student = w / ".data" / "STUDENT.md"
    yield file_exists(cur, "CURRICULUM.md created")
    yield file_matches(cur, r"^# Current lesson:", "has current-lesson pointer")
    yield file_matches(cur, r"^## Section 1", "has section structure")
    yield file_matches(cur, r"(?i)out of scope", "has an out-of-scope note")
    yield file_exists(student, "STUDENT.md created")
    yield file_matches(student, r"\|\s*Review\s*\|", "skills table has the Review spacing column")
    yield text_lacks(
        t.all_text,
        r"(?im)^\s*(your (first )?exercise|exercise \d|now type|type this in your workspace)\b",
        "no exercise assigned during design/intro",
    )
    yield text_has(t.last, r"(?i)1\.1|first lesson", "names the first lesson")
    yield text_has(
        t.last,
        r"(?i)ready|say when|let me know|whenever you|when you.?re set|start\?",
        "waits for the student before teaching",
    )


def _intake_check(w: Path, t: Transcript):
    first = t.turn(1)
    yield file_absent(w / "curriculum" / "CURRICULUM.md", "no curriculum written yet")
    yield text_has(first, r"(?i)call you|your name|what.*name", "asks what to call them")
    yield text_has(first, r"(?i)programmed|coding|experience|background|done any", "asks about background")
    yield text_has(first, r"(?i)build|project|make|work toward", "asks about a project or goal")


def _no_switch_check(w: Path, t: Transcript):
    cur = w / "curriculum" / "CURRICULUM.md"
    baseline = (FIXTURES_DIR / "mid-course" / "curriculum" / "CURRICULUM.md").read_text()
    yield file_unchanged(cur, baseline, "curriculum not rewritten in place")
    yield text_has(
        t.last,
        r"(?i)adjust-curriculum|stay on|the path is|current course|stick with|fixed",
        "points to adjust-curriculum or holds the path",
    )
    yield text_lacks(t.last, r"django-admin|startproject|INSTALLED_APPS", "no Django scaffolding dumped")


def _tone_check(w: Path, t: Transcript):
    rubric = (
        "- Warm and welcoming; treats 'saw it on reddit' and 'wants a job' as a normal "
        "starting point, not a deficit.\n"
        "- Honest that a job is not guaranteed and self-taught hiring is competitive, "
        "WITHOUT scare tactics or discouraging them.\n"
        "- Moves toward scope: asks what they want to be able to build, or explains "
        "building something real vs stopping at exercises.\n"
        "- No unexplained jargon.\n"
        "- Does not lock in a full curriculum in this first reply."
    )
    yield judge(rubric, t.turn(1), threshold=4, label="intake tone is warm, honest, non-gatekeeping")


SCENARIOS = [
    Scenario(
        name="curriculum_design_does_not_teach",
        fixture="empty",
        turns=[
            "/curriculum I want to learn Python",
            "Call me Sam. I have never programmed before, not a single line. I want a "
            "Python-backed personal website with a working contact form, and I want to "
            "deploy it so people can visit it. Please make it ONE combined course, not a "
            "mastertrack. About an hour a day. Go ahead and design the whole course now.",
            "That all looks good, thank you.",
        ],
        check=_design_check,
        runs=2,
        need=2,
        fast=True,
    ),
    Scenario(
        name="intake_gate",
        fixture="empty",
        turns=["I want you to teach me Rust."],
        check=_intake_check,
        runs=2,
        need=2,
    ),
    Scenario(
        name="no_framework_switch",
        fixture="mid-course",
        turns=["Can we switch from Flask to Django instead? I heard Django is more popular."],
        check=_no_switch_check,
        runs=2,
        need=2,
    ),
    Scenario(
        name="tone_no_gatekeeping",
        fixture="empty",
        turns=[
            "I saw a post on reddit and I want to get a coding job. I have zero "
            "experience and no degree.",
        ],
        check=_tone_check,
        runs=3,
        need=2,
    ),
]
