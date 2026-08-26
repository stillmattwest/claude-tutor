# Cursor Tutor

Rules and skills that turn Cursor into a curriculum designer and coding mentor for whatever you want to learn.

## How to use

1. Copy this repo into a folder dedicated to what you want to learn.
2. Open a chat and run the curriculum skill (`/curriculum`), then describe your goal.

```
/curriculum I want to learn web development with Python and FastAPI
```

Cursor will ask what to call you, your background, and skill level, then write `curriculum/CURRICULUM.md` divided into sections and lessons, plus a living `.data/STUDENT.md` (name, strengths, growth areas, and a skills table keyed by lesson ID). That file is how the tutor remembers you in the next chat.

After that, chat normally. The tutor rule keeps Cursor on the current lesson: explain, show examples for new syntax, check understanding, give exercises you type yourself in `workspace/`, and advance only when the lesson’s end goal is met. It reads `.data/STUDENT.md` so explanations match what you already handle well and where you still need practice.

### Layout

| Folder | What lives there |
|--------|------------------|
| `workspace/` | Your projects and the files you type |
| `curriculum/` | The course (`CURRICULUM.md`) and lesson summaries |
| `.data/` | Tutor notes about you (profile, skills table) — out of the way; you can still open it |
| `.cursor/` | Tutor rules and skills |

### Useful skills

| Skill | When to use |
|-------|-------------|
| `/curriculum` | Design or fully redesign the course |
| `/adjust-curriculum` | Mid-course pace, skip, or capstone changes |
| `/teach-lesson` | Start or continue the current lesson (tutor usually runs this) |
| `/stuck` | You’re blocked and want a hint, not the full answer |
| `/code-review` | Feedback on exercise code (one win, one improvement) |
| `/check-understanding` | Quiz / teach-back on the current lesson |
| `/complete-lesson` | Lesson end goal met (tutor usually runs this) |
| `/section-review` | Section end goal met or you want a section checkpoint |
| `/student-profile` | Create or refresh `.data/STUDENT.md` (name, strengths, skills table) |

## What you get

- **Progression with checkpoints** — Each section and lesson has a start point and a verifiable end goal. A section’s end goal is the next section’s start point.
- **No black boxes** — When a framework or tool shows up, Cursor explains how it works in plain language before treating it as magic.
- **Active practice** — You write the code. Cursor reviews it in chat, names problems, and lets you fix them.
- **Hint ladder when stuck** — Smallest useful hint first; full solutions only if you ask.
- **Lesson summaries** — After each lesson, a short summary under `curriculum/lesson_summaries/` you can revisit later.
- **Student profile** — `.data/STUDENT.md` remembers your name, strengths, growth areas, and a skills table (one row per lesson: `not started` / `learning` / `shaky` / `mastered`).

## Status

Core loop is in place: tutor mode plus skills for curriculum design, mid-course adjustment, stuck help, quizzes, lesson completion, section review, and a living student profile — with safety rails and fixed formats for lesson summaries and `.data/STUDENT.md`.
