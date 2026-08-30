---
name: introduce-course
description: Half-lesson introduction when a curriculum is ready to start. Use after writing curriculum/CURRICULUM.md, when the student begins a course, or when they ask for a course roadmap or introduction. On a mastertrack, include how the course fits the map; mindset is full (no map), skipped (first track course), or a brief re-commit (later track courses).
---

# Introduce Course

A **half-lesson** post (about half the length of `introduce-mastertrack`) when a live `curriculum/CURRICULUM.md` is ready. Roadmap of this course, renew enthusiasm, then wait — do not teach the first lesson in this turn.

## Instructions

1. Read `curriculum/CURRICULUM.md` and `.data/STUDENT.md` if it exists. Use the name they asked you to use.
2. In a mastertrack? Only if `curriculum/MASTERTRACK.md` exists. If it does, also read that map and `.data/MASTERTRACK.md`. Missing map = standalone course.
3. **First course on a track:** the current map item is the first item with **Type:** `curriculum` (usually `C1`). Later archived steps under `curriculum/tracks/` mean this is **not** the first course.
4. Deliver the introduction below. Keep it **about half** a lesson — one post unless a split is truly needed. No code. Do not list every lesson; walk **sections** and what they unlock.
5. Name the first lesson. **Stop.** Do not follow `teach-lesson` until they are ready.

## Required shape (half-lesson)

**Roadmap** — What this course is for (course / section end goals in plain language). The path through the sections in order. What “done” looks like. If this is a **standalone** course and `CURRICULUM.md` has **Out of scope**, say it once (honest, not a scare).

**Where it sits (mastertrack only)** — If there is **no** map, omit this block. If there is a map: where this course is on the track, what they already finished, and what this course unlocks next (next course, milestone, or capstone). Do not reteach the whole track.

**Enthusiasm** — A short, genuine spark for *this* course — what they will be able to do that they cannot do today. Not empty cheerleading.

**Mindset** (pick exactly one)

- **No mastertrack** — Give the mindset speech: patience, consistency, not rushing. Remind them that you are here to answer questions and mentor them every step of the way.
- **Mastertrack, first course** — Skip mindset entirely. They just heard it on the track intro.
- **Mastertrack, later course** — Do **not** repeat the full speech. Brief reminder only, then tell them this is a great opportunity to re-focus and re-commit.

## Do not

- Teach the first lesson in the same turn.
- Give the full mindset speech on a later track course, or any mindset block on the first track course.
- Explain how the course fits a mastertrack when there is no map.
- Dump `CURRICULUM.md` verbatim or start a quiz.

## Examples

- `/curriculum` FastAPI only (no map) → section roadmap, enthusiasm, full mindset + mentor reminder, wait for 1.1.
- Track C1 Python just written → section roadmap, how Python sits first on the track, enthusiasm, **no** mindset, wait for 1.1.
- Track C3 FastAPI after a pause → section roadmap, where FastAPI sits (after Python, Postgres, and a build week), enthusiasm, brief reminder + re-focus and re-commit, wait for 1.1.
