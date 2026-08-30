---
name: student-profile-format
description: Living student profile template for .data/STUDENT.md. Use when creating or editing .data/STUDENT.md (typically from the student-profile skill).
---

# Student Profile Format

When creating or editing `.data/STUDENT.md`, use this structure. Keep narrative sections short; the **Skills** table is the lookup.

```markdown
# Student

- **Name:**
- **Goes by:**
- **Pronouns:** (omit this line if unknown)

## Background

One short paragraph from intake (what they want to learn, prior experience).

## Strengths

- Cross-cutting habits (not a copy of `mastered` rows)

## Growth areas

- Cross-cutting practice targets (not a copy of `shaky` rows)

## Skills

Status is one of: `not started` · `learning` · `shaky` · `mastered`

| ID | Skill | Status | Last reviewed | Review | Note |
|----|-------|--------|---------------|--------|------|
| 1.1 | Files, folders, and the terminal | mastered | 2.1 | near | Independent after one hint |
| 1.2 | Git: stage and commit | shaky | 1.4 | soon | Mixes `add` and `commit` |
| 1.3 | Functions and return values | learning | — | — | Current lesson |
| 1.4 | Tests with pytest | not started | — | — | |

## Preferences

- How they like to learn, if known (omit this section if none)

## Tutor notes

- Session-to-session facts that help the next chat (omit if none)
```

**Skills table rules**

- One row per lesson in `curriculum/CURRICULUM.md`. **ID** is the lesson number (`1.2`). **Skill** is the lesson title (shorten if needed). If there is no live `CURRICULUM.md` (mastertrack designed, first step not started), **omit** the Skills table.
- Look up a skill by **ID**. Update that row in place; never add a second row for the same ID.
- **Last reviewed** and **Review** are spacing data for the `review` skill (see below). Blank (`—`) while a row is `not started` or `learning`; filled once it is `mastered` or `shaky`.
- **Note** is optional and short (what was hard, or `—` if nothing to say).
- **Strengths** / **Growth areas** are only for habits that are not a single curriculum row (e.g. “reads error messages before asking”). Do not duplicate the table there.
- Omit unused optional headings (**Preferences**, **Tutor notes**, **Pronouns**).

**Last reviewed / Review columns (spacing)**

- **Last reviewed** — the lesson ID at which the skill was learned or last recalled successfully. `complete-lesson` sets it to the lesson just finished; `review` bumps it to the current lesson on a solid recall.
- **Review** — how soon the skill is due for a retrieval check:
  - `soon` — due after ~1–2 further lessons
  - `near` — due after ~3–5
  - `far` — due after ~8–12
  - `retired` — overlearned; not scheduled (still checked if it is a shaky prerequisite for the current lesson)
- A solid recall in `review` promotes the bucket one step (`soon → near → far → retired`). A shaky or missing recall resets it to `soon` and sets **Status** to `shaky`.
- `complete-lesson` starts every newly `mastered` / `shaky` row at `soon`.
- Rows marked `mastered` at **intake** (already demonstrated, never taught here) start at **Review** `far` with **Last reviewed** `—`; `review` treats a `—` anchor as the first lesson when counting elapsed lessons.
