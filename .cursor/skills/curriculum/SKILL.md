---
name: curriculum-design
description: Designs or fully redesigns a CURRICULUM.md with sections, lessons, start points, and verifiable end goals. Use when CURRICULUM.md is missing or the user wants a from-scratch rewrite. For mid-course pace, skip, or capstone tweaks, use adjust-curriculum instead.
---

# Curriculum Design

## Goal

Design a path that teaches what the student asked for, paced and scoped to their **skill level from intake**, that a **senior developer in that space** would recognize as correct: modern tooling, sound foundations, and habits that transfer to real projects—not shortcuts that feel easy now and become expensive later.

Skill-appropriate does **not** mean outdated, toy-only, or “skip the boring parts seniors rely on.” Match depth, prior assumptions, and vocabulary to what intake revealed; still introduce the right practices at the right moment, with verifiable end goals. Skip or compress foundations they already demonstrated; teach foundations they lack before building on them.

## Instructions

### Intake (stop and ask if unknown)

- For mid-course changes that keep completed lessons (pace, skip known topics, capstone tweak), stop and use the `adjust-curriculum` skill instead of rewriting everything.
- Ensure you know what the user wants to learn. If you do not, stop and ask.
- Ensure you know if the user wants to build a particular type of learning project. If not, stop and ask. If they do not have one in mind, that is okay; if they do, build the curriculum around it.
- Ensure you know the user's programming background. If you do not, stop and ask. Be specific. Labels like "beginner" and "intermediate" are too vague.

### Protect them from what they don't know

- Prefer the **current default good path** for the language, framework, and project type (packaging, project layout, testing, env/config, version control, and other norms seniors expect). Example: prefer `uv` for new Python projects over ad-hoc `pip` unless the domain truly requires otherwise.
- Include **foundation topics the student did not ask for** when those topics are prerequisites for doing the desired skill well (e.g. a minimum of Git, tests, or project structure before a web API course). Keep those sections lean and justified by the end goal—do not pad.
- If the student requests an approach a senior would consider outdated, fragile, or misleading for learning, **do not silently adopt it**. Briefly say what you recommend instead and why (one or two sentences), then design the curriculum on the sound path unless they insist after hearing the tradeoff.
- Optimize for **transfer**: habits and mental models that still look right on the next project, not one-off tutorial magic that only works in this repo.
- Sequence so each new tool or practice appears when it first matters, with a plain-language “what / why” baked into that lesson’s end goal—not as an unexplained black box later.

### Structure

- Divide the curriculum into sections with a logical progression.
- Each section: start point (from skill level + prior sections) and a verifiable end goal.
- Each section contains lessons; each lesson: start point and verifiable end goal; ~30 minutes per lesson.
- Lessons follow a logical progression. A section’s end goal is the next section’s start point.
- Be a good mentor: do not use vocabulary that is likely new without defining it in an earlier or the same lesson’s scope.

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
