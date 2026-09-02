---
name: session-log-format
description: Format for the append-only session log at .data/SESSIONS.md (one row per day — lessons touched, review results, and where to resume). Use when creating or editing .data/SESSIONS.md.
---

# Session Log Format

`.data/SESSIONS.md` is a short, append-only log so the next chat can pick up
cleanly and the `review` skill can tell how long it has been since the last
session. Keep it terse — it is a ledger, not a journal.

Create it lazily the first time a session does something worth logging (a lesson
touched, a review run). It is tutor bookkeeping — keep it out of the student's
daily view; they can still open it.

```markdown
# Sessions

| Date | Lessons touched | Reviewed | Resume / notes |
|------|-----------------|----------|----------------|
| 2026-08-27 | 1.3, 1.4 | — | Section 1 done |
| 2026-08-29 | 2.3 (started) | 1.2 solid, 2.1 shaky | Mid 2.3 Part 2 — resume at the loop exercise |
```

**Rules**

- **Append only.** Newest row at the bottom. Never rewrite history to tidy it.
- **One row per calendar day.** Update today's row as the session goes; start a
  new row on a new date.
- **Date** — `YYYY-MM-DD`.
- **Lessons touched** — lesson IDs worked on this session; mark `(started)` if
  left mid-lesson, else assume completed. `—` if none (e.g. a review-only visit).
- **Reviewed** — skills checked by the `review` skill and how they went
  (`1.2 solid`, `2.1 shaky`). `—` if no review ran.
- **Resume / notes** — one short line: where to pick up next time, or a
  milestone marker. Keep it current when stopping mid-lesson. The exact spot
  inside a lesson lives in that lesson's saved plan (`.data/.lessons/...`,
  `## Progress` → `Resume at:`); this column just names the lesson and part, e.g.
  `Mid 2.3 Part 2 — see lesson plan`.

Written by `teach-lesson` (start / update today's row, keep **Resume** current),
`complete-lesson` (record the finished lesson), and `review` (record results).
Read by `review` (gap detection) and `teach-lesson` (pick up **Resume**, then
read the lesson plan for the exact part).
