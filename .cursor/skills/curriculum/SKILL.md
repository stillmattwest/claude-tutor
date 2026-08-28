---
name: curriculum-design
description: Designs or fully redesigns curriculum/CURRICULUM.md with sections, lessons, start points, and verifiable end goals. Use when that file is missing or the user wants a from-scratch rewrite. If the goal is clearly several full topics, offer a mastertrack vs one course. For mid-course pace, skip, or capstone tweaks, use adjust-curriculum instead. For topic-order changes on an existing mastertrack, use adjust-mastertrack.
---

# Curriculum Design

## Goal

Design a path that teaches what the student asked for, paced and scoped to their **skill level from intake**, that a **senior developer in that space** would recognize as correct: modern tooling, sound foundations, and habits that transfer to real projects—not shortcuts that feel easy now and become expensive later.

Skill-appropriate does **not** mean outdated, toy-only, or “skip the boring parts seniors rely on.” Match depth, prior assumptions, and vocabulary to what intake revealed; still introduce the right practices at the right moment, with verifiable end goals. Skip or compress foundations they already demonstrated; teach foundations they lack before building on them.

Stay **encouraging and welcoming throughout** intake and design—especially with beginners. Warm tone, no gatekeeping, no jargon flexing. Treat common entry paths (“Reddit,” “a friend said so,” “I want a job”) as normal, not deficits.

## Instructions

### Mastertrack (do not damage the single-curriculum path)

- If `curriculum/MASTERTRACK.md` is **missing**, skip this subsection. Intake and design below are unchanged.
- If a map exists **and** you are writing the live course for a **mapped curriculum item** (student asked to start that step, or the `mastertrack` skill handed off here): **skip intake**. Read `.data/STUDENT.md` and `.data/MASTERTRACK.md`. Use that item’s start/end and its 3–4 track skills as the spine: **one section per track skill**, lessons ~30 minutes under each. Then write `curriculum/CURRICULUM.md` as usual and follow `student-profile` (replace the lesson Skills table only; keep identity / strengths / growth). The `mastertrack` skill sets `.data/IN_MASTERTRACK_CURRICULUM` to `on`. Then follow `introduce-course`. Do not teach the first lesson in this turn.
- If a map exists and they want to change **topics or order**, stop and use `adjust-mastertrack`. For pace/lessons inside the *live* course only, use `adjust-curriculum`.
- If **no** map, and after inferring scope the honest path is **several full topics** (each would be its own course), **offer** a mastertrack vs one combined course. Wait. If they want a mastertrack, stop and use the `mastertrack` skill — do not write `CURRICULUM.md` in this turn. If they want one course, continue here.

### Intake (stop and ask if unknown)

- Skip this intake when the mastertrack subsection above says to (map exists and this is a mapped step).
- For mid-course changes that keep completed lessons (pace, skip known topics, capstone tweak), stop and use the `adjust-curriculum` skill instead of rewriting everything.
- Ensure you know **what to call them** (name / goes-by). If you do not, stop and ask.
- Ensure you know what the user wants to learn. If you do not, stop and ask.
- Ensure you know if the user wants to build a particular type of learning project. If not, stop and ask. If they do not have one in mind, that is okay; if they do, build the curriculum around it.
- Ensure you know the user's programming background. If you do not, stop and ask. Be specific. Labels like "beginner" and "intermediate" are too vague.

**Before writing `CURRICULUM.md`:** follow [infer-scope.md](infer-scope.md). Do not lock the course until any required scope question is answered. Mapped live-course writes skip that file (the map item is the scope).

After intake (and after writing `curriculum/CURRICULUM.md`), explain to the student that you are customizing their course and that is might take a few minutes. Then, follow the `student-profile` skill: create or update `.data/STUDENT.md` with name, background, and a **Skills** table with one row per lesson. Mark skills they already demonstrated as `mastered`; leave the rest `not started` and set the first lesson to `learning`. The student’s learning project lives in `workspace/`. Then follow the `introduce-course` skill before teaching (skip if the mapped-step bullet already did). Do not start lesson 1.1 in the same turn as design.

### Structure

- Divide the curriculum into sections with a logical progression.
- Each section: start point (from skill level + prior sections) and a verifiable end goal.
- Each section contains lessons; each lesson: start point and verifiable end goal; ~30 minutes per lesson.
- Lessons follow a logical progression. A section’s end goal is the next section’s start point.
- Be a good mentor: do not use vocabulary that is likely new without defining it in an earlier or the same lesson’s scope.
- If you ask a user to install a framework in one lesson, the next lesson should be a high-level walkthrough of the framework's structure. If this framework is the core of the curriculum (i.e "teach me Ruby on Rails") **ensure they get a good foundation in core concepts before moving on**. For example: If they are learning Rails, it is worth a lesson to talk about the MVC pattern and how it relates to Rails.
- If you are teaching a complex framework, talk about its design philosophies. e.g is it batteries-included or unopinionated? Discuss benefits and tradeoffs. Again, it is important the user has a good foundation before diving into implementation details. 

## CURRICULUM.md template

Write `curriculum/CURRICULUM.md` in this shape. Keep a current-lesson line at the top so the tutor rule can find it. Design exercises so the student’s files live in `workspace/`.

```markdown
# Current lesson: 1.1 First lesson title

**Out of scope:** Short list of what this course will not cover (plain language). Omit only if the course is the entire goal with no honest gaps.

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
