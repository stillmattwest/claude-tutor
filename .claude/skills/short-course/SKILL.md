---
name: short-course
description: Designs curriculum/CURRICULUM.md as a short course — at most five lessons on the highest-leverage skills for one narrow topic, taught at full depth. Use when the student wants a fast, focused footing rather than full coverage. For a complete multi-section course use curriculum; for several topics use mastertrack.
---

# Short Course Design

## What a short course is

A short course is a **focused, standalone mini-course of at most five lessons** on
one topic. It is written into `curriculum/CURRICULUM.md` with a
`**Type:** short course` marker line, so the rest of the tutor — `teach-lesson`,
`review`, `tutor-review`, `stuck`, `complete-lesson`, the session log — treats it
like any other live course.

Use it when the student wants a **fast, high-level footing** in a topic: "give me
the important parts of X," a weekend introduction, a targeted boost before they
start building. Not a career path, not full coverage.

## Scope discipline (this is the whole point)

The value of a short course is **ruthless selection**, not compression.

- **Five lessons is a hard ceiling.** Fewer is good. You may not exceed it. If the
  topic genuinely cannot be served in five lessons, say so plainly and recommend
  the `curriculum` skill instead — do not try to squeeze a full course into five.
- **Do not cram.** Each lesson gets a real explain -> show -> practice cycle at
  normal lesson depth (~30-45 minutes), the same as a full course. A short course
  has *fewer* lessons, never *thinner* ones. Rushing five shallow lessons past the
  student is a failure, not a short course.
- **Still delivered in parts.** `teach-lesson` runs these lessons like any other —
  its "split complex lessons into parts" rule fully applies, with teach-back
  checks between parts. A slightly longer lesson means *more* parts, never one
  long dump. Design each lesson so it breaks cleanly into two or three focused
  pieces.
- **Pick the highest-leverage skills.** Ask: of everything in this topic, which
  three to five things unlock the most for someone who has none of it yet? Teach
  those properly. Everything else goes in **Out of scope**.
- If one lesson's end goal lists six sub-topics, you are cramming — cut scope,
  do not pack the lesson.
- **No sections.** A short course is a flat list of lessons numbered `1`-`5`.

## Instructions

### Not for mastertracks

If `curriculum/MASTERTRACK.md` exists, a short course does not apply — the live
course is (or will be) a mapped step. Tell the student and route to the
`mastertrack` or `adjust-mastertrack` skill. Do not write a short course over a
track.

### Replace an existing live course

Before writing anything, follow
[../curriculum/archive-live-course.md](../curriculum/archive-live-course.md).

### Intake (stop and ask if unknown)

Keep it short — a short course needs less intake than a full course.

- What to call them (name / goes-by).
- The **topic**, specific enough to bound five lessons ("React state," not
  "frontend").
- Their programming background, specific — labels like "beginner" are too vague.
  Enough to set each lesson's start point.
- Whether there is something they want to build with it (optional; use it to
  judge which skills are highest-leverage).

Do **not** run the full ship test in
[../curriculum/infer-scope.md](../curriculum/infer-scope.md). A short course is
honest by design about being a starting point — the end-of-course handoff below
carries that. Still apply two things from that file: prefer the **current default
good path** (senior-correct tooling and foundations, not shortcuts), and **write
what it will not cover**.

### Design

- Course-level **Start point** (what the student can already do) and **End goal**
  (what they can do after five lessons).
- Up to five lessons, each with a **Start point** and a **verifiable End goal**.
  A lesson's end goal is the next lesson's start point.
- Logical progression. Do not use vocabulary you have not defined in this or an
  earlier lesson.
- If the topic is a framework and it fits, spend an early lesson on its core model
  or design philosophy before implementation details — but only if that still
  leaves room for the hands-on skills inside five lessons.
- Add a short **Out of scope** note in plain language. A short course always has
  honest gaps; name them, including that this is a starting point, not full
  coverage.

### After writing

1. Tell the student you are customizing their short course and it may take a
   moment.
2. Follow the `student-profile` skill: create or update `.data/STUDENT.md` with
   name, background, and a **Skills** table with one row per lesson (IDs `1`-`5`).
   Mark anything they already demonstrated `mastered`; set lesson `1` to
   `learning` and the rest `not started`. Their work lives in `workspace/`.
3. Follow the `introduce-course` skill (it has a short-course branch). Do **not**
   teach lesson `1` in the same turn as the design.

## CURRICULUM.md template (short course)

```markdown
# Current lesson: 1 First lesson title

**Type:** short course

**Out of scope:** Short plain-language list of what these lessons do not cover,
including that this is a fast starting point, not full coverage of the topic.

**Start point:** What the student can already do.
**End goal:** What the student can do when the short course is done.

### 1 First lesson title
**Start point:** ...
**End goal:** ...

### 2 Second lesson title
**Start point:** The previous lesson's end goal.
**End goal:** ...
```

## End of the short course

The last lesson has no next lesson, so when its end goal is met `complete-lesson`
runs this handoff instead of a plain "complete" note: celebrate what the student
can now do, then offer three honest next steps and let them sit with it — no
pressure to choose now.

1. **Go deeper** — start a full `/curriculum` on the same topic for real
   coverage.
2. **Another short course** — `/short-course` on the next piece, with its start
   point set to where this one left off.
3. **Go build** — take these skills into a project in `workspace/` and come back
   for more when they hit the edges.

## Do not

- Exceed five lessons, or pack several sub-topics into one lesson to stay under
  the cap.
- Water down lesson depth to fit more material in.
- Use sections.
- Write a short course when a mastertrack exists (route to `adjust-mastertrack`).
- Overwrite a live course without following `archive-live-course.md` first.
- Offer alternate stacks or frameworks — the topic they named is the topic. Path
  changes go to `adjust-curriculum`.
- Teach lesson `1` in the same turn as the design.

## Examples

- `/short-course the essentials of Git` for someone who can code but has never
  used version control -> five lessons: what a repo is, stage/commit,
  branch/merge, remotes and push/pull, undoing mistakes. Out of scope: rebase,
  submodules, CI. End: offer a full Git curriculum, a follow-on short course on
  collaboration workflows, or go use it on a real project.
- Student asks for "everything about React" -> too big for five lessons; say so,
  recommend `/curriculum`, and offer a short course scoped to one slice (e.g.
  "React components and state") instead.
