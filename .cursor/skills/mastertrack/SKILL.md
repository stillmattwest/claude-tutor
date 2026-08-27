---
name: mastertrack
description: Designs a multi-topic mastertrack map with curriculum steps, milestone projects, and a capstone. Use when the student wants a mastertrack, a sequence of full courses, or a path that is clearly several topics rather than one curriculum. Also use when starting the next map item or completing a track curriculum step.
---

# Mastertrack

A mastertrack is a **map of skills** plus standalone projects. Each map skill has a start point and end goal. Write a full `CURRICULUM.md` only when the student **arrives** at that curriculum step.

If `curriculum/MASTERTRACK.md` is **missing**, this skill does not apply to the daily lesson loop. Single-curriculum behavior is unchanged.

Follow the `mastertrack-format` rule for file shapes. Milestone and capstone teaching: [projects.md](projects.md). End of a track course: [complete-step.md](complete-step.md).

## Compatibility

- Do **not** require this skill when there is no map.
- Do **not** write `curriculum/CURRICULUM.md` while designing the track.
- Create `.data/IN_MASTERTRACK_CURRICULUM` with the single line `off`. Missing flag file means `off`.

## Design (intake once)

Stop and ask if unknown (same bar as `curriculum`):

- What to call them (name / goes-by).
- What they want to learn (outcome, not only a tool name).
- Whether they have a learning-project idea (optional).
- Programming background — specific, not “beginner/intermediate.”

If the goal is “get a job,” give the same honest disclaimer as the `curriculum` skill, then continue.

Stay encouraging. Prefer the current default good path for each topic (senior-correct tooling and foundations). Infer full scope and **ask** before locking topics; do not silently inflate or omit.

### Build the sequence

1. Split the goal into **curriculum steps** — each step is a topic that deserves its own later `CURRICULUM.md` (not a light survey).
2. Each curriculum step gets **three or four** track skills, each with start point and end goal.
3. Insert a **milestone** after every **two** curriculum steps. Leftover unpaired step sits before the capstone (no extra milestone).
4. End with a **capstone** (~2–3 weeks) that uses the whole track.
5. Milestones (~1 week) and the capstone are map items with **Steps** (accomplishments). No code in the map.

Example cadence: `Python → Postgres → Milestone A → FastAPI → Tailwind → Milestone B → Capstone`.

### Write files

1. `curriculum/MASTERTRACK.md` — the map. Current item = first curriculum step, status `not started`.
2. `.data/MASTERTRACK.md` — all track skills `not started`. Current item = that first step, status `not started`.
3. `.data/IN_MASTERTRACK_CURRICULUM` — `off`.
4. Follow `student-profile`: create `.data/STUDENT.md` with name, background, strengths/growth if known. **Omit the Skills table** until a live `CURRICULUM.md` exists.

Do **not** write `curriculum/CURRICULUM.md`.

Tell them the track in plain language (steps, when they will build, what the capstone is). Name the first item. **Wait** — do not start step 1 until they say to.

## Start the next item

Use when they agree to begin the current/next map item (after design, or after a pause).

1. Read the map, `.data/MASTERTRACK.md`, and the flag.
2. If current status is `paused`, the next item is the one named in the pause (or the next unfinished item on the map).
3. Branch on **type**:

**Curriculum**

- Follow the `curriculum` skill with **no intake**. Seed the live course from this item’s start/end and its 3–4 track skills (one **section** per track skill; lessons under each section).
- Follow `student-profile`: keep identity / strengths / growth / preferences / tutor notes; **replace** the Skills table with one row per new lesson. First lesson `learning`, rest `not started`.
- Write `.data/IN_MASTERTRACK_CURRICULUM` as `on`.
- Set current item to this step, status `learning`, in both MASTERTRACK files.
- Set this step’s first track skill to `learning` in `.data/MASTERTRACK.md`.
- Name the first lesson and wait.

**Milestone or capstone**

- Flag stays `off` (or write `off`).
- Set current item to this project, status `learning`.
- Follow [projects.md](projects.md). Do not write or require `CURRICULUM.md`.

## Completing a curriculum step

When the last lesson of the last section is done **and** the flag is `on`, follow [complete-step.md](complete-step.md). Do not use that file if the map is missing or the flag is `off`.

## Completing a milestone or capstone

Handled in [projects.md](projects.md). After a milestone: pause (same choice as complete-step). After the capstone: mark the track complete.

## Do not

- Write every topic’s `CURRICULUM.md` at design time.
- Run a second intake when the flag is `on` or when starting a mapped curriculum item.
- Auto-start the next item after a course or project finishes.
- Put milestone/capstone work inside `CURRICULUM.md`.
- Change topics or order (use `adjust-mastertrack`).
- Teach a map item that is not current.

## Examples

- `/mastertrack I want professional web development from scratch` → intake, write map + progress, flag `off`, wait to start C1.
- Student: “Let’s start PostgreSQL” after a pause → no intake, write that step’s `CURRICULUM.md`, flag `on`.
- Student finishes the last FastAPI lesson with flag `on` → `complete-lesson` then [complete-step.md](complete-step.md), not “course over.”
