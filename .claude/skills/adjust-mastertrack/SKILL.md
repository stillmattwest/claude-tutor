---
name: adjust-mastertrack
description: Mid-track replan that keeps completed mastertrack items and rewrites the remaining map. Use when the student wants to change topics, skip a future course, add or drop a step, or retarget the capstone on an existing mastertrack. For a single live course's pace or lessons, use adjust-curriculum instead.
---

# Adjust Mastertrack

Use only when `curriculum/MASTERTRACK.md` exists. If it does not, this skill does not apply (use `adjust-curriculum` or `curriculum`).

## Instructions

1. Read `curriculum/MASTERTRACK.md`, `.data/MASTERTRACK.md`, `.data/IN_MASTERTRACK_CURRICULUM` (missing = `off`), and `.data/STUDENT.md` if it exists.
2. Ask only what you still need: which future items to change, any hard constraints.
3. **Keep** completed map items (curriculum steps already archived under `curriculum/tracks/`, finished milestones, their track-skill rows). Do not renumber or delete finished ids unless the student explicitly asks.
4. **Rewrite forward** from the first unfinished map item (or from an agreed restart). Update remaining curriculum steps (3–4 skills each, start/end goals), then **rebuild future milestones** so one still sits after every **two remaining** curriculum steps. Leftover unpaired future step sits before the capstone. Keep the capstone last; retarget its **Uses** and end goal to the new remaining track.
5. Do **not** write or replace live `CURRICULUM.md` unless they are **between** items (flag `off`, status `paused` / `not started`) **or** they explicitly want the unused tail of the **current** course rewritten — then use `adjust-curriculum` for lesson-level changes, not this skill.
6. If the flag is `on`, do not archive or swap the live course here. Change only **future** map items. Tell them the live course continues until they finish it or ask to abandon it.
7. Sync `.data/MASTERTRACK.md`: keep status on track-skill ids that remain; add rows for new skills (`not started`); drop future skills that were never started. Completed rows stay.
8. Keep `# Current item:` and progress **current item** consistent. Follow `mastertrack-format`. Update **Out of scope** if the remaining path’s honest gaps changed (if they drop shipping from a professional-role track, the first out-of-scope bullet must say they will not yet be able to ship a product).
9. Briefly tell them what changed and what the next item is. Do not auto-start it.

## Do not

- Replace the whole track from scratch (use `mastertrack` for a new map, and only if they want to abandon this one).
- Insert a new intake.
- Erase archived courses under `curriculum/tracks/`.
- Put milestones inside a `CURRICULUM.md`.
- Recalculate milestones that are already complete.

## Examples

- Python mastered, Postgres not started: “drop Postgres, add SQLite” → C1 untouched; rewrite C2 and later; rebuild **future** milestones only.
- “I want the capstone to be a deployed personal site” → keep finished steps; rewrite remaining items and capstone end goal so they still chain.
- Flag `on` in the middle of FastAPI: “skip Tailwind later” → live FastAPI stays; later map items change.
