---
name: review
description: Short interleaved retrieval practice on older skills so they do not fade. Use as a session warm-up when earlier skills are due, or when the student asks to review, warm up, be quizzed on old material, or check whether they still remember something. For the current lesson use check-understanding; for a section end goal use section-review.
---

# Review

Spaced retrieval practice. Pull a few recall questions on **older** `mastered` /
`shaky` skills and interleave them, so knowledge from earlier lessons does not
decay. This skill **never advances the curriculum** and never writes a lesson
summary — it only updates mastery / spacing data and the session log.

Not the same as:

- `check-understanding` — quizzes the **current or last** lesson.
- `section-review` — checkpoint against a **section end goal**.

If `.data/STUDENT.md` has no Skills table (mastertrack map designed, no live
`CURRICULUM.md` yet), there is nothing to review — say so briefly and stop.

## Instructions

1. Read `.data/STUDENT.md` (Skills table), `curriculum/CURRICULUM.md` (lesson
   order and the current lesson's **Start point**), and `.data/SESSIONS.md` if it
   exists (for the last-session date). In a mastertrack, also read
   `.data/MASTERTRACK.md`.
2. Build the **due set** (see *What is due* below).
3. If nothing is due: say the student is current, offer an optional quick recall
   anyway if they asked for `/review`, and stop. Do not manufacture a warm-up.
4. Ask **2–4** interleaved questions (up to **~6** for an explicit `/review`, or
   scope to a topic the student named). Prefer spoken / written recall; escalate
   to a tiny typed snippet only for a `shaky` skill.
5. Score each answer **solid / shaky / missing** (same vocabulary as
   `check-understanding`). Name misconceptions in plain language.
6. Apply *Results* below: update each checked row via the `student-profile` skill
   and append the outcome to today's `.data/SESSIONS.md` row (per
   `session-log-format`).
7. Hand back to whatever comes next (the lesson, the project step, or nothing).

## What is due

A `mastered` / `shaky` row is **due** when **either**:

- **Lessons elapsed** since its **Last reviewed** lesson ID ≥ its **Review**
  bucket threshold. Count intervening rows in the ordered Skills table — do not
  do date arithmetic.
  - `soon` — due after ~1–2 further lessons
  - `near` — due after ~3–5
  - `far` — due after ~8–12
  - `retired` — not scheduled; only checked if it is a shaky prerequisite for the
    current lesson
- **Long gap** — ~10+ days since the last `.data/SESSIONS.md` row **and** the row
  is `shaky` or a prerequisite for the current lesson. A long absence widens the
  net.

Order the due set:

1. `shaky` + due — actively at risk.
2. `mastered` + due **and** a prerequisite for the current or next lesson —
   inferred from the current lesson's **Start point** and topical overlap with
   earlier lesson titles / summaries. Surface these right before they are needed.
3. `mastered` + due, oldest **Last reviewed** first.

Cap at 2–4 for a warm-up (~6 for `/review`). Interleave topics; do not stack
several questions on one skill unless it is `shaky` and needs a deeper check.

## Question sources and style

Draw from `curriculum/lesson_summaries/<section>/<lesson>.md` (Concepts /
Commands / APIs / What you built), and archived
`curriculum/tracks/*/lesson_summaries/` in a mastertrack. Prefer **generative
recall**: teach-back, predict-the-output, "write one line that…", "A vs B — when
would you use each", spot-the-bug. Keep the tone a warm-up, not an exam. Under
~5 minutes for a warm-up.

## Auto warm-up (before `teach-lesson`)

Tutor mode runs this at the start of a teaching session when skills are due.

1. Due set empty → proceed to the lesson silently.
2. Otherwise: "Quick warm-up before we start — a few questions on earlier
   material." Ask 2–4 interleaved questions.
3. The student may **skip** — **unless** a due skill is a prerequisite for
   today's lesson and a quick check shows it `shaky` / `missing`. Then shore it
   up first: a brief re-show or mini-recap; if it is badly gone, recommend
   pausing new material to rebuild it before teaching the lesson.
4. Score, update data, log, then continue to `teach-lesson`.

## `/review` on demand

The student names a topic ("review me on functions") or leaves it open (pick the
most-overdue set). Up to ~6 items. Runnable any time, including during a
mastertrack milestone or capstone — reviewing that project's **Uses** course
skills before a build week is encouraged.

## Results

- **solid** → promote the **Review** bucket one step (`soon → near → far →
  retired`); set **Last reviewed** to the current lesson; **Status** unchanged,
  or `shaky → mastered` if it is clearly solid now.
- **shaky** → **Review** = `soon`; **Status** → `shaky`; refresh the **Note**.
- **missing** → **Review** = `soon`; **Status** → `shaky`; if it is a
  prerequisite for today's lesson, re-show before proceeding; otherwise note it
  and either give one small remediation exercise now or leave it for the next
  warm-up.
- Update rows via `student-profile`. Append what was reviewed and how it went to
  today's `.data/SESSIONS.md` row.

## Do not

- Advance the curriculum, write a lesson summary, or start the next lesson /
  section / map item.
- Review the **current** lesson (that is `check-understanding`).
- Turn the warm-up into a full new lesson on a weak skill — note it, hand back a
  small fix or defer, and move on.
- Block the session on an optional warm-up. Only the shaky-prerequisite case
  gates progress.
- Paste full solutions; ask for recall first.

## Examples

- Student returns at lesson 3.1 after finishing section 2 → warm-up pulls 3
  interleaved questions from sections 1–2 summaries, one on a `shaky` Git row;
  Git comes back shaky again → bucket stays `soon`, Note refreshed, then teach 3.1.
- `/review` right after a lesson, nothing due → "You're current — nothing's due
  for review. Want a quick recall anyway, or jump into the next lesson?"
- `/review comprehensions` mid-course → 3–4 questions scoped to that skill; solid
  across the board → bucket `near → far`, Last reviewed bumped to the current lesson.
- Three-week gap, then a session → last `SESSIONS.md` row is 21 days old, so
  `shaky` rows and current-lesson prerequisites are all pulled in, not just the
  bucket-due ones.
