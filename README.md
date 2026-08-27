# Cursor Tutor

Rules and skills that turn Cursor into a curriculum designer and coding mentor for whatever you want to learn.

## How to use

1. Copy this repo into a folder dedicated to what you want to learn.
2. Open a chat and run **`/curriculum`** for one course, or **`/mastertrack`** for a sequence of full courses plus build projects.

```
/curriculum I want to learn FastAPI
```

```
/mastertrack I want professional web development from scratch
```

For a single course, Cursor asks what to call you, your background, and skill level, then writes `curriculum/CURRICULUM.md` divided into sections and lessons.

For a mastertrack, it writes a **map** (`curriculum/MASTERTRACK.md`) of topics — each with a few skills, start points, and end goals — plus milestone projects and a capstone. It does **not** write each topic’s full course until you get there. If you run `/curriculum` with a goal that is clearly several full topics, Cursor will offer a mastertrack vs one combined course and wait.

After a live course exists, chat normally. The tutor rule keeps Cursor on the current lesson: explain, show examples for new syntax, check understanding, give exercises you type yourself in `workspace/`, and advance only when the lesson’s end goal is met.

### Layout

| Folder | What lives there |
|--------|------------------|
| `workspace/` | Your projects and the files you type |
| `curriculum/` | The live course (`CURRICULUM.md`), lesson summaries, and (if you have one) the mastertrack map |
| `curriculum/tracks/` | Archived courses from finished mastertrack steps |
| `.data/` | Student profile, mastertrack progress, and the in-curriculum flag |
| `.cursor/` | Tutor rules and skills |

### Useful skills

| Skill | When to use |
|-------|-------------|
| `/curriculum` | Design or fully redesign one course |
| `/mastertrack` | Design a multi-topic track (courses + milestones + capstone) |
| `/adjust-curriculum` | Mid-course pace, skip, or capstone changes (this course only) |
| `/adjust-mastertrack` | Change remaining topics, order, or the track capstone |
| `/teach-lesson` | Start or continue the current lesson (tutor usually runs this) |
| `/stuck` | You’re blocked and want a hint, not the full answer |
| `/code-review` | Feedback on exercise code (one win, one improvement) |
| `/check-understanding` | Quiz / teach-back on the current lesson |
| `/complete-lesson` | Lesson end goal met (tutor usually runs this) |
| `/section-review` | Section end goal met or you want a section checkpoint |
| `/student-profile` | Update your personal information |

## What you get

- **Progression with checkpoints** — Each section and lesson has a start point and a verifiable end goal. A section’s end goal is the next section’s start point.
- **No black boxes** — When a framework or tool shows up, Cursor explains how it works in plain language before treating it as magic.
- **Active practice** — You write the code. Cursor reviews it in chat, names problems, and lets you fix them.
- **Hint ladder when stuck** — Smallest useful hint first; full solutions only if you ask.
- **Lesson summaries** — After each lesson, a short summary under `curriculum/lesson_summaries/` you can revisit later.
- **Mastertrack (optional)** — Several full courses in sequence, a milestone build after every two courses, and a larger capstone. Finishing a course pauses with a recap of where you are on the track; the next course is written only when you start it.

## Status

Core loop is in place: tutor mode plus skills for curriculum design, mid-course adjustment, stuck help, quizzes, lesson completion, and section review — with safety rails and a fixed lesson-summary format. Mastertrack is available as a map-plus-projects path on top of that loop.
