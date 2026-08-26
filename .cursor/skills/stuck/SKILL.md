---
name: stuck
description: Helps a blocked student with a hint ladder without dumping the full solution. Use when the student says they are stuck, blocked, lost, or asks for a hint.
---

# Stuck

## Instructions

1. Confirm the current lesson end goal in one sentence (from `curriculum/CURRICULUM.md`).
2. Ask what they tried and what happened (error text, unexpected behavior, or where they froze). If they already said, skip this.
3. Give the **smallest** next hint that unblocks progress — a question, a concept nudge, or where to look — not the finished code.
4. If they are still stuck after that hint, escalate one step (narrower hint or a short example of a *related* idea). Do not paste their full solution unless they **explicitly** ask you to write the code.
5. When they are moving again, resume normal tutor mode for the current lesson.

## Do not

- Skip straight to the answer on the first request for help.
- Rewrite their project files in `workspace/` unless they explicitly ask.
- Change the curriculum or jump to a later lesson.

## Examples

- Student: "I'm stuck on the routing part." → Restate the goal, ask what they tried, hint at matching path to handler — no full route file.
- Student: "Just give me the code." → Provide only what they asked, then resume tutor mode.
