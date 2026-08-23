---
name: curriculum-design
description: Designs or fully redesigns a CURRICULUM.md with sections, lessons, start points, and verifiable end goals. Use when CURRICULUM.md is missing or the user wants a from-scratch rewrite. For mid-course pace, skip, or capstone tweaks, use adjust-curriculum instead.
---

# Curriculum Design

## Goal

Design a path that teaches what the student asked for, paced and scoped to their **skill level from intake**, that a **senior developer in that space** would recognize as correct: modern tooling, sound foundations, and habits that transfer to real projects—not shortcuts that feel easy now and become expensive later.

Skill-appropriate does **not** mean outdated, toy-only, or “skip the boring parts seniors rely on.” Match depth, prior assumptions, and vocabulary to what intake revealed; still introduce the right practices at the right moment, with verifiable end goals. Skip or compress foundations they already demonstrated; teach foundations they lack before building on them.

Stay **encouraging and welcoming throughout** intake and design—especially with beginners. Warm tone, no gatekeeping, no jargon flexing. Treat common entry paths (“Reddit,” “a friend said so,” “I want a job”) as normal, not deficits.

## Instructions

### Intake (stop and ask if unknown)

- For mid-course changes that keep completed lessons (pace, skip known topics, capstone tweak), stop and use the `adjust-curriculum` skill instead of rewriting everything.
- Ensure you know what the user wants to learn. If you do not, stop and ask.
- Ensure you know if the user wants to build a particular type of learning project. If not, stop and ask. If they do not have one in mind, that is okay; if they do, build the curriculum around it.
- Ensure you know the user's programming background. If you do not, stop and ask. Be specific. Labels like "beginner" and "intermediate" are too vague.

### When the goal is “get a job”

“I just want to get a job” (or similar) is a very common answer. Handle it carefully and kindly:

1. **Be honest without crushing hope.** You cannot guarantee anyone a job. Landing an entry-level role as a self-taught coder is hard and competitive—say so plainly, without scare tactics or false promises.
2. **Say what this path *can* do.** Set a solid foundation: real skills, senior-correct habits, and projects that demonstrate ability. Getting started on the right foot matters; this is a long journey, and completing a first curriculum is a meaningful first stretch—not the whole road.
3. **Invite building later.** After they finish, they can ask to extend or redesign the curriculum (portfolios, interview prep, deeper stack, etc.). Do not pretend one course equals employment.
4. **Then continue design.** Once that disclaimer (or similar) is clear, proceed with intake, scope inference, and `CURRICULUM.md` as usual—still encouraging and welcoming.

### Infer full scope (context-aware)

Named tools and stack buzzwords are often a proxy for a larger goal—especially when the student is early in their journey (e.g. they saw “Python + FastAPI” on Reddit or a friend suggested it). Before writing `CURRICULUM.md`:

1. **Infer the likely real outcome** from their ask, background, and project idea. Example: a new programmer asking for FastAPI often wants to **ship a working website or web app**, not an API-only specialty. An experienced backend engineer asking for the same may want FastAPI depth only.
2. **Map the gap** between what they named and what that outcome usually requires (adjacent skills, missing layers of the stack, ops/deploy basics, etc.).
3. **With beginners, explain the basics before asking about scope.** Define any terms the question needs in one or two plain sentences first (e.g. what people see in the browser vs what the server does behind the scenes). Do not ask about “front-end” vs “API” until those ideas mean something—otherwise the question is confusing and the answer is useless.
4. **Propose the fuller scope and ask**—do not silently inflate or silently omit. Phrase the question for their skill level:
   - Early learners: outcome language only, after the brief definitions (“Do you want to learn enough to build the pages people click around in, or focus on the server part that sends and stores data?”).
   - Experienced learners: sharper tradeoffs (“API-only FastAPI track, or full-stack with a minimal front end and how they talk to each other?”).
5. **Wait for their answer** on material scope before locking the curriculum. If they decline adjacent topics, design a coherent narrower path and note what it will *not* cover so expectations stay honest.
6. Still apply the senior-correct bar inside whatever scope they choose—fuller scope is about completeness of the goal, not an excuse for outdated shortcuts.

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
