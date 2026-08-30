---
name: check-understanding
description: Quizzes the student on the current or last completed lesson and remediates gaps. Use when the student asks to quiz them, check understanding, or review what they learned.
---

# Check Understanding

This skill targets the **current or last** lesson. For retention checks on
**older** skills, use `review`. Both score answers as solid / shaky / missing.

## Instructions

1. Read `.data/STUDENT.md` if it exists. Identify the target: the **current lesson** in `curriculum/CURRICULUM.md`, or the last completed lesson if they ask to review that. Lean quiz questions toward Skills-table rows with status `shaky` (and toward growth areas) when they overlap this lesson.
2. Ask 3–5 short questions (teach-back, “what would happen if…”, or “why this way”). Prefer spoken/written answers over coding at first.
3. Score each idea briefly: solid / shaky / missing. Name misconceptions in plain language.
4. Give **one** remediation exercise they type themselves for the weakest gap.
5. Follow the `student-profile` skill if scores change the picture (solid → that row `mastered`; shaky/missing → `shaky`, and growth areas only if it is a cross-cutting habit).
6. Do **not** advance the curriculum or write a lesson summary. That happens only when the lesson end goal is met via `complete-lesson`.

## Do not

- Turn the quiz into a full new lesson on unrelated topics.
- Paste long solutions when checking understanding; ask them to explain or try first.

## Examples

- Student: "Quiz me." → Questions on the current lesson’s end goal concepts, then one fix-up exercise if needed.
- Student: "Do I get lesson 1.2?" → Clarify this skill does not advance lessons; report readiness against the end goal only.
