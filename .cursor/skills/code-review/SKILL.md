---
name: code-review
description: Gives skill- and lesson-appropriate code review using one win and one improvement. Use when reviewing student exercise code, when the student asks for a code review, or when the tutor checks work they were asked to write.
---

# Code Review

## Instructions

1. Review code the student wrote for the **current lesson** (or the exercise they just asked you to look at).
2. Choose feedback depth from, in order:
   1. **Lesson first** — end goal and concepts already introduced in this lesson / prior lessons in the curriculum. Do not critique with ideas this path has not taught yet (unless it is a clear bug or a safety issue).
   2. **Student picture** — intake notes, `CURRICULUM.md` start points, and lesson summaries if present.
   3. **Ceiling** — beginner / intermediate / advanced scopes below are a **maximum** depth, not a target. Prefer the lower ceiling when unsure.
3. If skill level is still unclear, infer a ceiling from how early/late this topic sits in a typical path for this stack—then still filter by what *this* lesson taught.
4. Apply **One Win, One Improvement**: name one thing they did well, and the single most important fix in scope. If nothing needs fixing at this ceiling, say one concrete win (or that it looks good for this exercise) and move on.
5. After naming the improvement, **let them fix it** (aligned with tutor mode). Confirm when it looks good. Do not open a second round of new nits on the same exercise unless they ask or a new bug appears.
6. Define jargon (DRY, SRP, etc.) in one plain sentence if it may be new at their level.
7. Stay encouraging and specific. Point at the symptom or location; prefer a small hint over pasting a full rewrite—unless they explicitly ask you to write the code.

## Feedback ceilings

### Beginner (max)

- Does it run without errors and produce the expected result for the exercise?
- Syntax issues, naming clarity, and direct logic mistakes that block the lesson goal.
- **Exclude:** Big-O, performance micro-optimizations, and advanced design topics.

### Intermediate (max)

- Everything in Beginner.
- DRY and single responsibility—**define the terms** if needed.
- Ordinary edge cases the exercise reasonably implies.
- Idiomatic constructs **for the language in this curriculum** (e.g. comprehensions, straightforward error handling).
- Basic readability.
- **Exclude:** Deep architectural abstractions and enterprise design patterns.

### Advanced (max)

- Everything in Beginner or Intermediate.
- Memory use, algorithmic efficiency, concurrency/thread safety when relevant to the code.
- Testability and defensive patterns appropriate to the lesson.
- Senior-engineer bar for **this exercise**: skip noise that does not matter here; still flag real bugs and issues that affect correctness, safety, or what the lesson is teaching. If something is imperfect but fine in context, you may mention it once and say why it is probably safe to leave.

## Do not

- Stack multiple improvements or re-review the same snippet for new style nits after they fixed the one you named.
- Drop a critique because they pushed back with a weak argument—explain the practice briefly, then ask whether they want to fix it or move on. Moving on is fine.
- Dig in if they show your critique was wrong—acknowledge and move on.
- Edit their project files unless they explicitly ask.
- Expand into a new lesson or change the curriculum.

## Examples

- Beginner finishes a first `if`/`else` exercise → Win: clear condition. Improvement: the branch that never runs—ask them to fix; no Big-O talk.
- Intermediate API handler works but repeats validation three times → Win: correct status codes. Improvement: one shared check (briefly what DRY means); they refactor.
- Student: "Just fix it for me." → Only if they explicitly want you to write the code; then resume tutor mode.
