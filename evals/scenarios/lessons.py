"""Lesson-loop scenarios: completion bookkeeping, review warm-up, the stuck ladder."""

from __future__ import annotations

import re
from pathlib import Path

from assertions import (
    file_matches,
    file_unchanged,
    glob_exists,
    judge,
    text_has,
    text_lacks,
)
from common import Result
from harness import FIXTURES_DIR, Scenario, Transcript


def _data_rows(path: Path) -> int:
    if not path.exists():
        return 0
    rows = 0
    for line in path.read_text().splitlines():
        s = line.strip()
        if s.startswith("|") and "---" not in s and not re.search(r"\|\s*Date\s*\|", s):
            rows += 1
    return rows


def _complete_check(w: Path, t: Transcript):
    cur = w / "curriculum" / "CURRICULUM.md"
    student = w / ".data" / "STUDENT.md"
    sessions = w / ".data" / "SESSIONS.md"

    summaries = list(w.glob("curriculum/lesson_summaries/**/2.1*.md"))
    yield glob_exists(w, "curriculum/lesson_summaries/**/2.1*.md", "2.1 lesson summary written")
    if summaries:
        s = summaries[0].read_text()
        headings = sum(
            bool(re.search(p, s, re.M))
            for p in (r"^##\s*Concepts", r"^##\s*Commands", r"^##\s*What you built")
        )
        yield Result("summary has the standard headings", headings >= 3, f"{headings}/3 found")

    yield file_matches(cur, r"^# Current lesson:\s*2\.2", "current-lesson pointer advanced to 2.2")
    yield file_matches(
        student,
        r"\|\s*2\.1\s*\|[^|\n]*\|\s*(mastered|shaky)\s*\|",
        "2.1 row marked mastered or shaky",
    )
    yield file_matches(
        student,
        r"\|\s*2\.1\s*\|[^|\n]*\|\s*(?:mastered|shaky)\s*\|\s*2\.1\s*\|\s*soon\s*\|",
        "2.1 spacing columns set (Last reviewed 2.1, Review soon)",
    )
    yield Result(
        "SESSIONS.md gained a new row",
        _data_rows(sessions) >= _data_rows(FIXTURES_DIR / "mid-course" / ".data" / "SESSIONS.md") + 1,
        f"{_data_rows(sessions)} rows now",
    )


def _warmup_check(w: Path, t: Transcript):
    first = t.turn(1)
    yield file_matches(
        w / "curriculum" / "CURRICULUM.md", r"^# Current lesson:\s*2\.1", "still on lesson 2.1"
    )
    yield text_lacks(
        first,
        r"(?i)@app\.route|from flask import|render_template",
        "did not jump straight into teaching Flask",
    )
    yield text_has(
        first,
        r"(?i)function|list|dict|variable|return value",
        "recall touches earlier section-1 skills",
    )
    rubric = (
        "- Before teaching lesson 2.1, the tutor runs a short warm-up: a few recall "
        "questions or prompts about EARLIER lessons (functions, lists/dicts, variables).\n"
        "- It does NOT immediately start teaching lesson 2.1 (Flask routes).\n"
        "- The warm-up is framed as quick, and the student is free to skip it."
    )
    yield judge(rubric, first, threshold=4, label="a spaced-review warm-up precedes the lesson")


def _stuck_check(w: Path, t: Transcript):
    app = w / "workspace" / "app.py"
    baseline = (FIXTURES_DIR / "mid-course" / "workspace" / "app.py").read_text()
    yield file_unchanged(app, baseline, "did not edit the student's app.py")
    yield file_matches(
        w / "curriculum" / "CURRICULUM.md", r"^# Current lesson:\s*2\.1", "still on lesson 2.1"
    )
    yield judge(
        "The reply helps a stuck student with a hint, a question, or a pointer to where "
        "to look. It does NOT contain a complete working Flask app or a full solution to "
        "the exercise.",
        t.turn(1),
        threshold=4,
        label="first stuck reply is a hint, not the answer",
    )
    yield judge(
        "The student is still stuck. The reply escalates to a smaller hint or a tiny "
        "example of a RELATED idea. It still does not paste a complete runnable Flask "
        "app with the route that solves their exercise.",
        t.turn(2),
        threshold=4,
        label="second stuck reply escalates without dumping the solution",
    )


SCENARIOS = [
    Scenario(
        name="complete_lesson_bookkeeping",
        fixture="mid-course",
        write_before={
            1: {
                "workspace/app.py": (
                    "from flask import Flask\n\napp = Flask(__name__)\n\n\n"
                    '@app.route("/")\ndef index():\n'
                    '    return "<h1>Sam\'s site</h1><p>Welcome to my first Flask app.</p>"\n'
                )
            }
        },
        turns=[
            "I finished lesson 2.1. workspace/app.py is saved with a `/` route that "
            "returns an `<h1>` and a `<p>`. I ran `flask run`, opened "
            "http://localhost:5000 in my browser, and both the heading and the "
            "paragraph render.",
            "Yes, the saved file matches what's in the browser.",
            "I'm happy with it. Let's move on to 2.2.",
        ],
        check=_complete_check,
        runs=2,
        need=2,
        fast=True,
    ),
    Scenario(
        name="review_warmup_fires",
        fixture="mid-course",
        turns=["I'm back after a couple of weeks off. Let's do the next lesson."],
        check=_warmup_check,
        runs=3,
        need=2,
        fast=True,
    ),
    Scenario(
        name="stuck_no_dump",
        fixture="mid-course",
        turns=[
            "I'm stuck on the lesson 2.1 exercise. I don't even know how to start the Flask app.",
            "I tried but it's still not working and I'm lost.",
        ],
        check=_stuck_check,
        runs=3,
        need=2,
    ),
]
