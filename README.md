# Cursor Tutor

Rules and skills that turn Cursor into a curriculum designer and coding mentor for whatever you want to learn.

## How to use

1. Copy this repo into a folder dedicated to what you want to learn.
2. Open a chat and run the curriculum skill (`/curriculum`), then describe your goal.

```
/curriculum I want to learn web development with Python and FastAPI
```

Cursor will ask about your background and skill level, then write a `CURRICULUM.md` divided into sections and lessons.

After that, chat normally. The tutor rule keeps Cursor on the current lesson: explain, check understanding, give exercises you type yourself, and advance only when the lesson’s end goal is met.

## What you get

- **Progression with checkpoints** — Each section and lesson has a start point and a verifiable end goal. A section’s end goal is the next section’s start point.
- **No black boxes** — When a framework or tool shows up, Cursor explains how it works in plain language before treating it as magic.
- **Active practice** — You write the code. Cursor reviews it in chat, names problems, and lets you fix them.
- **Lesson summaries** — After each lesson, Cursor writes a short summary under `lesson_summaries/` you can revisit later.

## Status

Early days: one rule (`tutor-mode`) and one skill (`curriculum`). In practice that already produces a usable learning path — more coming later.
