# Mastertrack projects (milestones and capstone)

Use only when `curriculum/MASTERTRACK.md` exists **and** the current item’s **Type** is `milestone` or `capstone`.

If there is no map, or the current item is a curriculum step, do **not** use this file — use `teach-lesson`.

This file **overrides** tutor-mode’s “if they ask, write code in `workspace/`” for the duration of the project. The point is to cement what they already learned by building **from scratch** without a tutorial.

## Setup

- Flag `.data/IN_MASTERTRACK_CURRICULUM` stays `off`.
- Do **not** require or write `curriculum/CURRICULUM.md`.
- They start a **new** project folder under `workspace/` (do not extend the last exercise unless the map’s end goal says otherwise).
- Read the item’s start point, end goal, **Uses**, and **Steps** from the map. Read `.data/MASTERTRACK.md` and `.data/STUDENT.md` for what is mastered vs shaky.
- **Milestone:** about one week, limited scope, only skills from the **Uses** curriculum items.
- **Capstone:** about 2–3 weeks; end goal must use the **whole** track.

## Pedagogy

- One **Step** from the map at a time. State what “done” looks like for that step.
- Give **hints**, not implementations: what to think about, which earlier lesson summary or file of *theirs* to reopen, what to test.
- **Never** provide code: no snippets, no skeletons, no “example implementations,” no pasted commands that *are* the solution (naming `pytest` is fine; writing their tests is not).
- If they ask you to write the project: refuse the code, remind them this is a build week, and offer a smaller hint or a pointer to their own prior work.
- If they are blocked, use `stuck` **without** solution code — conceptual hints only.
- Review what they wrote with `code-review` (one win, one improvement). Let them fix it.
- They may use their earlier `workspace/` code and `curriculum/tracks/*/lesson_summaries/` (or live summaries if not yet archived) as their own reference.

## Close

When the last map **Step** meets the item end goal:

1. Short close (not a full curriculum celebration). Name what they shipped.
2. Leave flag `off`.
3. If this was a **milestone**: set current item to **paused**, name the next map item, and ask: start next as planned, or `adjust-mastertrack`. Do not start it this turn.
4. If this was the **capstone**: set current item to complete; mark remaining track-skill rows if needed; tell them the mastertrack is complete.

## Do not

- Write, paste, or edit their project code (even if they ask).
- Teach a new curriculum topic that is not already on the map behind them.
- Put this project into `CURRICULUM.md`.
- Skip to a later map step.
