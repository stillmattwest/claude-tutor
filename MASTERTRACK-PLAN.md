# Mastertrack implementation plan

Temporary design doc. Delete this file when implementation is done.

## Goal

A **mastertrack** is a sequence of full curricula plus standalone projects. It is a map of skills (start point + end goal), not one giant light survey. Each topic gets a real `CURRICULUM.md` only when the student arrives at that step.

**Packaging (Option C):** a `mastertrack` design skill, plus small guarded updates to the existing tutor loop (`tutor-mode`, `curriculum`, `complete-lesson`, `student-profile`). Do not invent a parallel teaching engine.

**Compatibility:** if `curriculum/MASTERTRACK.md` is missing, behavior is unchanged. Track logic only runs when that file exists. Single-curriculum remains the default path, not a special case of mastertrack.

## Product rules

1. **Map, not curricula up front.** The track lists skills with start points and end goals (like sections/lessons). Do not write `CURRICULUM.md` until the student gets to that step.
2. **Coarse progress in `.data`.** Separate from the lesson-level Skills table. Each curriculum step has only three or four mastertrack-level skills (e.g. “basic Python data structures” = one mastered skill).
3. **Intake once.** A simple datapoint in `.data` records whether the live course is a mastertrack curriculum. When that flag is `on`, a new curriculum must **not** run a new intake form; fill `.data/STUDENT.md` from mastertrack records (identity, strengths, growth areas).
4. **`adjust-mastertrack`.** Student can request changes to the remaining track. Keep completed items; rewrite forward.
5. **Finish a topic by pausing.** Do not silently start the next course. Celebration is a **lesson-sized** post: summarize the curriculum just completed and place it in the track (what they have accomplished and where they are going). Then offer “start the next item as planned” or `/adjust-mastertrack`.
6. **Milestone projects.** Not part of any `CURRICULUM.md`. Separate map items. From scratch, limited scope, about **one week**. Steps give **hints, not code**. One milestone after every **two curriculum steps**. Purpose: cement what they have learned by building with it.
7. **Capstone.** Last map item. About **2–3 weeks**. Incorporates everything in the track. Same pedagogy as milestones (hints, no code).

## File contract

| Piece | Path | Role |
|--------|------|------|
| Map | `curriculum/MASTERTRACK.md` | Student-visible ordered items: curriculum steps (3–4 skills each, each with start/end), milestones, capstone. |
| Progress | `.data/MASTERTRACK.md` | Coarse skills + current item. Status: `not started` · `learning` · `shaky` · `mastered`. |
| Flag | `.data/IN_MASTERTRACK_CURRICULUM` | One line: `on` or `off`. `on` = live `CURRICULUM.md` is a track step (skip intake). `off` during milestones, capstone, pauses, and any single-curriculum student. |
| Live course | `curriculum/CURRICULUM.md` | Unchanged format. Written only when they arrive at a curriculum step. |
| Live profile | `.data/STUDENT.md` | Unchanged format. Lesson Skills table is **only** the current curriculum. Identity / strengths / growth persist across steps. |
| Archived courses | `curriculum/tracks/<slug>/` | Finished (and not-yet-active) topic curricula and lesson summaries. |

**IDs:** curriculum lesson IDs stay local (`1.2`). Coarse track skill IDs are namespaced (`py.datastructures`) so they never collide.

**Current item** lives in `.data/MASTERTRACK.md`. When a map exists, tutor-mode reads that first:

- Curriculum step + flag `on` → existing teach loop (`teach-lesson`, `complete-lesson`, …).
- Milestone or capstone → hint-only project loop (`mastertrack/projects.md`).
- Pause after a finished step → do not start the next course until they say so.

**Intake** happens once, on `/mastertrack`. Lazy `/curriculum` writes skip intake when the flag is `on`.

## Example shape

Four curriculum topics → two milestones + capstone:

`Python → Postgres → Milestone A → FastAPI → Tailwind → Milestone B → Capstone`

Milestone after every **two curriculum steps**; a leftover unpaired step sits before the capstone (five topics → milestones after 2 and 4, then the fifth, then capstone). `adjust-mastertrack` rebuilds **future** milestones only if remaining step count changes.

## Skills and hooks

### New

- **`mastertrack`** — Intake once. Write the map, progress file, and flag `off`. Place milestones and capstone. Do **not** write `CURRICULUM.md` until they start a step.
- **`adjust-mastertrack`** — Same spirit as `adjust-curriculum`: keep completed map items and progress rows; rewrite future steps / milestones / capstone.

### Existing, behind the compatibility check

- **`tutor-mode` / `workspace-layout`** — If no map, identical to today. If map exists, honor current item (course vs project vs pause).
- **`curriculum`** — Flag `on`: no intake; seed profile; write this step’s `CURRICULUM.md` from the step’s start/end and its 3–4 track skills (those are the spine of the course). No map: unchanged. Later: may *offer* a track for a clearly multi-topic ask, then wait.
- **`complete-lesson`** — Last lesson of last section **and** flag `on`: do not treat the journey as over; flag `off`; archive this course; lesson-sized celebration; pause.
- **`student-profile`** — On a lazy course write, do not replace identity / strengths / growth; swap only the lesson Skills table.

### Not a third student-facing command

Milestone and capstone teaching live in `.cursor/skills/mastertrack/projects.md`, loaded only when the current item is a project. Do **not** fold “never show code” into `teach-lesson`.

## Implementation steps

Approval gate after each step. Do not start the next step until the current verification passes.

### Step 1 — Contract only (no teaching behavior)

Write the map and progress templates, the flag convention, and a short format rule. Update `workspace-layout` to name the files. **Do not** change `complete-lesson` or `teach-lesson` yet.

**Verify**

- Grep core skills: no required reads of mastertrack files.
- A student with only `CURRICULUM.md` still matches today’s loop.
- Review templates against the web-dev example (map skills, milestone spacing, capstone) before any skill runs.

### Step 2 — `/mastertrack` design

Intake once. Write the map (skills with start/end, milestones every 2 steps, capstone). Write `.data/MASTERTRACK.md` with all coarse skills `not started`. Flag stays `off`. **Do not** write `CURRICULUM.md`.

**Verify**

- Dry-run a 3-step toy track (or the web-dev goal in chat).
- 3–4 skills per curriculum step; milestone after step 2; leftover step 3; capstone last; no `CURRICULUM.md` created.
- Single-curriculum path unused.

### Step 3 — Lazy curriculum + flag

“Start step 1” → `curriculum` skill with **no intake**, flag `on`, `STUDENT.md` identity from intake, Skills table from the new course, first lesson `learning`. Archive path: `curriculum/tracks/<slug>/`.

**Verify**

- Fake “arrive at step 1”: no second intake; flag `on`; `teach-lesson` still only reads `CURRICULUM.md`.
- Normal `/curriculum` with **no** map: full intake, no flag file.

### Step 4 — Finish a topic

`complete-lesson` last-lesson branch: lesson summaries as today, then archive course, update coarse skills in `.data/MASTERTRACK.md`, flag `off`, lesson-sized celebration, pause.

**Verify**

- Fixture: 1-section stub course marked complete. Must **not** say “course finished, goodbye.” Must **not** write the next `CURRICULUM.md` until they agree.
- Non-track student finishing a course still gets today’s “course complete” behavior.

### Step 5 — `/adjust-mastertrack`

Keep completed map items and progress rows. Rewrite future steps/milestones/capstone. Do not touch the live `CURRICULUM.md` except when they are between items (or they explicitly replan the unused tail of the current course).

**Verify**

- Fixture where Python is mastered: “drop Postgres, add SQLite” — Python rows untouched; milestone cadence recalculated for remaining curriculum steps only.

### Step 6 — Milestones

`projects.md`: from scratch, ~1 week, numbered steps, hints only, **no code / no pasteable solutions**. Tutor-mode: if current item is a milestone, follow this, not `teach-lesson`. Completing the last project step → short close, then same pause as step 4.

**Verify**

- Walk one milestone on a 3-step toy track.
- Tutor never writes project code. `CURRICULUM.md` not required. Flag stays `off`.

### Step 7 — Capstone

Same project engine, 2–3 week scope, end goal uses the whole map. Completing it marks the track complete.

**Verify**

- Capstone brief on the toy track depends on all curriculum steps; still no code from the tutor.

### Step 8 — Discoverability

README + `/curriculum` offer: “this looks like a multi-topic path — mastertrack or one course?” Default remains one course unless they opt in.

**Verify**

- `/curriculum I want FastAPI only` does not create a map.
- `/curriculum I want professional web dev from scratch` offers a track and waits.

## Defaults (locked unless we change them)

- Map is student-visible (`curriculum/MASTERTRACK.md`); progress and flag stay in `.data/`.
- Milestone after every two curriculum steps; leftover unpaired steps sit before the capstone.
- Designing the track does not write `CURRICULUM.md` until they start step 1.
- Implement in the order above; do not ship a live full web-dev track until step 2’s dry-run.

## Out of scope until a later step

- Changing `teach-lesson` pedagogy for normal lessons.
- Writing all topic curricula at track-creation time.
- A second lesson-level Skills table in `.data/STUDENT.md`.
- Auto-advancing to the next curriculum without the celebration/pause.
