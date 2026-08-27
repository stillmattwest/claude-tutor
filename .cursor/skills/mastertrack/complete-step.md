# Completing a mastertrack curriculum step

Use only when **all** of these are true:

- `curriculum/MASTERTRACK.md` exists
- `.data/IN_MASTERTRACK_CURRICULUM` is `on`
- The student just met the **last lesson** end goal of the **last section** of the live course

If the map is missing or the flag is `off` (or the file is missing), do **not** use this file. Finish `complete-lesson` as a normal single course.

Run this **after** the usual `complete-lesson` summary and `.data/STUDENT.md` lesson-row update for that last lesson.

## Archive and bookkeeping

1. **Track skills.** This course’s sections match this map item’s skills (`C1.1` ↔ section 1, …). For each, set the row in `.data/MASTERTRACK.md` to `mastered` or `shaky` from how independently they finished that section (hints, re-shows, quiz). Do not copy lesson IDs into the progress table.
2. **Archive.** Move the live course into `curriculum/tracks/<item-id>-<slug>/` (example: `curriculum/tracks/c1-python-foundations/`):
   - `curriculum/CURRICULUM.md`
   - `curriculum/lesson_summaries/` (the whole folder)
3. Write `.data/IN_MASTERTRACK_CURRICULUM` as `off`.
4. In both MASTERTRACK files, set **current item** to **paused** and name the **next** map item (milestone, next curriculum step, or capstone). If none, the track is complete — say so after the celebration and stop.

Do **not** write the next `CURRICULUM.md`. Do **not** start a milestone or capstone in the same turn.

## Celebration (required, lesson-sized)

Write this as a full lesson-shaped post, not a short toast. Split if it would be a wall of text. Do not dump code.

1. **Orient** — This course in one or two sentences (what it was for on the track).
2. **What they can do now** — The 3–4 track skills in plain language, tied to the item’s end goal. Mention shaky vs mastered honestly.
3. **Behind them** — Earlier map items (courses and milestones already done), in one short stretch.
4. **Ahead** — The next map item: what it is (course vs build week vs capstone) and why it comes next. Do not teach it.
5. **Thread** — One concrete way this course will show up in that next item (still no code).

Then **stop** and ask:

- Start the next item as planned, or
- Change the remaining track (`adjust-mastertrack`)

Wait for their answer.

## Do not

- Say the overall journey is finished when more map items remain.
- Auto-advance to the next curriculum or project.
- Re-run intake.
- Leave the flag `on` after archive.
