---
name: adjust-curriculum
description: Mid-course curriculum replan that keeps completed work and rewrites forward. Use when the student wants to change pace, skip known material, change the capstone, or tweak the path without a full redesign.
---

# Adjust Curriculum

## Instructions

1. Read `.data/STUDENT.md` if it exists, then `curriculum/CURRICULUM.md`. Note the current lesson and what is already completed (summaries under `curriculum/lesson_summaries/` and lessons before the current line). Use the Skills table (`mastered` / `shaky`) when deciding what to compress or revisit.
2. Ask only what you still need: what to change (too fast/slow, skip topics, new project goal) and any hard constraints.
3. **Keep** completed lessons and their summaries as-is. Do not renumber or delete finished work unless the student explicitly asks.
4. **Rewrite forward** from the current lesson (or from an agreed restart point): update remaining section/lesson titles, start points, and verifiable end goals so progression still chains (section end goal → next section start point).
5. Keep lessons ~30 minutes each. Preserve the **senior-correct** path for the stack already chosen (tooling, foundations, transferable habits)—same bar as `curriculum`. Do not quietly introduce outdated shortcuts to go faster. Do not offer alternate frameworks unless the student asks to change stack (that is closer to a full redesign — use the `curriculum` skill). If they ask to drop a foundation a senior would keep, explain the tradeoff briefly before rewriting.
6. Leave `# Current lesson:` in `curriculum/CURRICULUM.md` pointing at the lesson they should do next after the adjustment.
7. Follow `student-profile` if the adjustment changes what they already know vs still need (e.g. skipped material they demonstrated → that row `mastered`; sync table rows with the new lesson list).
8. Briefly tell the student what changed and what to do next.

## Do not

- Replace the entire curriculum from scratch (use `curriculum` / curriculum-design for that).
- Skip verifying end goals on rewritten lessons.
- Erase lesson summaries for completed lessons.

## Examples

- Student: "This is too slow; I already know Git." → Drop or compress upcoming Git lessons; keep past summaries; rewrite forward.
- Student: "I want the capstone to be a CLI instead of a web app." → Adjust remaining sections toward that end goal without wiping early sections already done.
