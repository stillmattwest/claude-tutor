---
name: curriculum-design
description: Designs a CURRICULUM.md with sections, lessons, start points, and verifiable end goals. Use when CURRICULUM.md is missing or the user asks to design or redesign a curriculum.
---

# Curriculum Design

## Instructions

- Ensure you know what the user wants to learn. If you do not, stop and ask.
- Ensure you know if the user wants to build a particular type of learning project. If not, stop and ask. If the user does not have a learning project in mind, that's okay. If they do, build the curriculum around it.
- Ensure you know the user's programming background. If you do not, stop and ask. Be specific with your questions to get a good idea of what the user's skill level is. Labels like "beginner" and "intermediate" are too vague to be useful.
- The curriculum should follow modern best practices for the type of project, language, and framework the user is interested in. For example, you should use uv in a Python project, not pip unless the type of project makes pip a hard requirement.
- A curriculum is divided into Sections, which should follow a logical progression.
- Each section should have a start point based on the user's skill level and the previous sections
- Each section should have a verifiable end goal
- Each section should contain lessons
- Each lesson should have a start point based on the section start point and goals and the previous lessons in the section.
- Each lesson should have a verifiable end goal
- lessons should follow a logical progression
- lessons should be designed for a single learning session of roughly 30 minutes.
- Be a good mentor. Do not use vocabulary that is likely new to the user without first defining it.

## CURRICULUM.md template

Write `CURRICULUM.md` in this shape. Keep a current-lesson line at the top so the tutor rule can find it.

```markdown
# Current lesson: 1.1 First lesson title

## Section 1: Section title
**Start point:** What the student can already do.
**End goal:** What the student can do when the section is done.

### 1.1 First lesson title
**Start point:** ...
**End goal:** ...

### 1.2 Second lesson title
**Start point:** ...
**End goal:** ...

## Section 2: Next section title
**Start point:** The previous section's end goal.
**End goal:** ...

### 2.1 First lesson in this section
**Start point:** ...
**End goal:** ...
```
