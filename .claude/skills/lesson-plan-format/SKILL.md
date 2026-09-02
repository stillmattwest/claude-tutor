---
name: lesson-plan-format
description: Saved lesson plan template for files under .data/.lessons/. Use when authoring or updating a lesson plan (typically from the teach-lesson skill), so a lesson can be resumed mid-way instead of regenerated.
---

# Lesson Plan Format

A **lesson plan** is the frozen delivery script for one lesson: its orientation,
the parts, the exact examples shown in chat, the exercise, and a progress
pointer. `teach-lesson` authors it the first time it delivers the lesson and then
**reuses it verbatim** on every later session so a student who left mid-lesson
picks up exactly where they stopped.

This is **not** the lesson summary. The summary
(`curriculum/lesson_summaries/...`, see `lesson-summary-format`) is a short
retrospective written at completion. The plan and the summary sit at parallel
paths and do different jobs.

## Path

`.data/.lessons/<NN-section-slug>/<N.N-lesson-slug>.md`

Use the **same** section-folder and lesson-file slugs as the lesson summary, e.g.
plan `.data/.lessons/02-a-first-flask-app/2.1-your-first-flask-route.md` alongside
summary `curriculum/lesson_summaries/02-a-first-flask-app/2.1-your-first-flask-route.md`.

For a **short course** (`curriculum/CURRICULUM.md` has `**Type:** short course`)
the file is flat — `.data/.lessons/<N-lesson-slug>.md`, no section folder — and
the heading is `# N Lesson title`.

## Template

```markdown
# 2.3 Handling form input

- **Lesson ID:** 2.3
- **End goal:** One sentence copied from CURRICULUM.md — what "done" looks like.
- **Built from end goal:** The exact CURRICULUM.md end-goal text this plan was authored from (staleness check).
- **Status:** in progress
- **Generated:** 2026-08-29

## Orient

What is new in this lesson vs review from earlier lessons.

## Part 1 — <one focus>

**Teach:** the plain-language points for this part.
**Show:** the exact minimal example to put in chat, with the one-line "what this line does".
**Check:** the teach-back / predict-the-output question before moving on.

## Part 2 — <one focus>

**Teach:** ...
**Show:** ...
**Check:** ...

## Exercise

**Prompt:** what they build, typed by them in `workspace/<path>`.
**Done when:** the observable check that meets the lesson end goal.

## Code review

What `tutor-review` should focus on for this exercise (the likely win, the likely improvement).

## Progress

- [ ] Part 1
- [ ] Part 2
- [ ] Exercise
- [ ] Code review
**Resume at:** Part 1
```

## Rules

- **Parts** match what `teach-lesson` shows the student — "Lesson 2.3 Part 1",
  "Part 2", not "Chunk 1". Number them in order. Simple lessons may have a single
  part; split complex ones per the `teach-lesson` rules.
- **`Resume at:`** is always exactly one of: `Part N`, `Exercise`, `Code review`,
  or `Done`. It is the single source of truth for where to pick up.
- **`Status:`** is `in progress` until the lesson end goal is met, then
  `complete` (set by `complete-lesson`).
- **Author once, then freeze.** On resume, only the `## Progress` block and
  `Status` line change. Do **not** rewrite Teach / Show / Exercise content, or
  swap in different examples — that is what makes a half-finished lesson stop
  matching the student's work.
- **Regenerate the whole file only when:** the plan is stale (its
  `Built from end goal:` no longer matches `CURRICULUM.md` — `teach-lesson`
  checks this), or the student explicitly asks to redo the lesson from scratch.
- Keep it terse. It is a script the tutor follows, not student-facing prose.

## Lifecycle

- **Written / updated by** `teach-lesson` — authors the file on first delivery,
  ticks `## Progress` and moves `Resume at:` as each part / the exercise / the
  review is finished.
- **Finalized by** `complete-lesson` — `Status: complete`, every item ticked,
  `Resume at: Done`. The file is kept, not deleted.
- **Read by** `teach-lesson` (resume), and by `stuck` / `check-understanding` so
  hints and quizzes match what was actually taught.
- **Deleted by** `adjust-curriculum` (non-`complete` plans for changed or dropped
  lessons) and `curriculum` (whole tree on a full redesign). Archived by
  `.claude/skills/mastertrack/complete-step.md` into
  `curriculum/tracks/<item-id>-<slug>/lessons/`.
