---
name: student-profile
description: Maintains a living .data/STUDENT.md (name, strengths, growth areas, and a skills table keyed by curriculum lesson ID). Use when starting a session, during curriculum intake, after a lesson/quiz/section review, or when the student shares their name or learning preferences.
---

# Student Profile

A good tutor remembers the person, not just the current lesson. `.data/STUDENT.md` is the durable student picture across chats. Curriculum skill status lives in the **Skills** table — look up a lesson by **ID**.

## When to read

Read `.data/STUDENT.md` (if it exists) before teaching, reviewing, quizzing, or adjusting the curriculum. Use the name they asked you to use. If `.data/MASTERTRACK.md` exists, read it too — those rows are **track-level** skills, not lesson IDs. Do not treat a `mastered` track skill as a foundation they still lack when writing or teaching a later mapped course.

From the **Skills** table:

- Do not re-teach rows with status `mastered` unless a later session shows they are `shaky` again.
- Spend more care on `shaky` rows when this lesson depends on them.
- `learning` is the current lesson; `not started` is still ahead.

If the file is missing, continue with the lesson or intake. Create it as soon as you have a name or other durable facts (intake, or the first time they tell you).

## When to write

Update `.data/STUDENT.md` when you have **new evidence**, without waiting to be asked:

- **Intake / curriculum design** — create the file (name, background) and a **Skills** table with **one row per lesson** in `curriculum/CURRICULUM.md`. Status `mastered` if they already demonstrated it; otherwise `not started`. Set the first lesson to `learning`. If a mastertrack was just designed and there is **no** live `CURRICULUM.md` yet, create identity/background and **omit** the Skills table until the first mapped course is written.
- **Mastertrack lazy course** — when writing `CURRICULUM.md` for a mapped step, **do not** re-run intake. Keep Name, Goes by, Pronouns, Background, Strengths, Growth areas, Preferences, Tutor notes. **Replace** only the Skills table (one row per new lesson). Coarse track skills stay in `.data/MASTERTRACK.md`, not in this table.
- **`complete-lesson`** — set that lesson’s **Status** to `mastered` or `shaky` from how independently they finished (hints, re-shows, quiz). Set the next lesson’s status to `learning` if it was `not started`.
- **`check-understanding` / `section-review` / `code-review`** — update that row’s **Status** / **Note** (and strengths / growth areas) when a **pattern** appears, not for a one-off typo.
- **`adjust-curriculum`** — sync rows with the rewritten lesson list: keep status on IDs that remain; add rows for new lessons (`not started`); drop future lessons that were never started. Completed rows stay.
- **They tell you** their name, pronouns, or how they like to learn.

Follow the `student-profile-format` rule for the table and headings.

## Evidence bar

- Write only what they **said** or you **observed** in their work. Do not invent a personality or diagnose them.
- Put skill-specific facts in the table **Note** for that ID (`needed two hints on KeyError`), not vague labels (“struggles with Python”).
- Strengths are real capabilities, not empty praise. Growth areas are practice targets, not character judgments. Neither section should repeat the Skills table.
- Prefer **replacing** a stale note or status over appending forever.
- Never put secrets, credentials, or unrelated personal data in `.data/STUDENT.md`.

## Do not

- Ignore their name once you know it.
- Use their name excessively; it sounds condescending.
- Treat a completed lesson as `mastered` if they only finished with heavy hints — set that row to `shaky`.
- Keep a second **lesson-level** mastered/shaky list outside the Skills table. Track-level skills belong in `.data/MASTERTRACK.md` only when a map exists.
- Duplicate `curriculum/CURRICULUM.md` or paste full lesson summaries into notes.
- Overwrite the whole file to restyle it; edit the rows and sections that changed.
