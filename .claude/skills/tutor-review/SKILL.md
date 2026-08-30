---
name: tutor-review
description: Gives skill- and lesson-appropriate code review using one win and one improvement; explains why broken code failed and shows parallel examples, not the exercise answer. Use when reviewing student exercise code, when the student asks for a code review, or when the tutor checks work they were asked to write.
---

# Tutor Review

## Instructions

1. Review code the student wrote for the **current lesson** (or the exercise they just asked you to look at).
2. Choose feedback depth from, in order:
   1. **Lesson first** — end goal and concepts already introduced in this lesson / prior lessons in the curriculum. Do not critique with ideas this path has not taught yet (unless it is a clear bug or a safety issue).
   2. **Student picture** — `.data/STUDENT.md` if present (Skills table + strengths / growth areas), `curriculum/CURRICULUM.md` start points, and lesson summaries.
   3. **Ceiling** — beginner / intermediate / advanced scopes below are a **maximum** depth, not a target. Prefer the lower ceiling when unsure.
3. If skill level is still unclear, infer a ceiling from how early/late this topic sits in a typical path for this stack—then still filter by what *this* lesson taught.
4. Apply **One Win, One Improvement**: name one thing they did well, and the single most important fix in scope. If nothing needs fixing at this ceiling, say one concrete win (or that it looks good for this exercise) and move on.
5. When something **did not work** (error, wrong output, or logic that misses the goal), follow **Explain why it failed** below—not just “that’s wrong.”
6. After naming the improvement, **let them fix it** (aligned with tutor mode). Confirm when it looks good. Do not open a second round of new nits on the same exercise unless they ask or a new bug appears.
7. Define jargon (DRY, SRP, etc.) in one plain sentence if it may be new at their level.
8. Stay encouraging and specific. Point at the symptom or location; prefer a small hint or illustrative example over pasting a full rewrite of their exercise—unless they explicitly ask you to write the code.
9. If the review reveals a **pattern** (not a one-off typo), follow `student-profile` to update that lesson’s Skills-table row (`shaky` / `mastered` / **Note**) or a cross-cutting growth area.

## Explain why it failed

When code errors, misbehaves, or misses the exercise goal:

1. **Infer intent** — What were they trying to accomplish? Read their names, structure, and comments; don’t assume malice or carelessness.
2. **Acknowledge it** — Say you see the goal in plain language (“You’re trying to loop until the user types quit—that part is right.”).
3. **Explain why it didn’t work** — Tie cause to effect: what the runtime/language actually did vs what they expected. Use their skill level; no jargon without a one-line definition.
4. **Show the correct *pattern* with a tiny parallel example** — Same idea, different names/context so it is **not** their exercise answer. Mark it clearly as an illustration, not something to paste.
5. **Hand back the fix** — Ask them to apply the pattern to their code. Do not drop in the finished solution unless they explicitly ask.

Example shape (not their exact code):

```python
# Illustration only — not your exercise
while True:
    answer = input("Continue? ")
    if answer == "quit":
        break
```

Then: “Try applying that loop/break shape to your version.”

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

- Paste the student’s exercise solution as the “example”—illustrations must be parallel, not the answer.
- Stack multiple improvements or re-review the same snippet for new style nits after they fixed the one you named.
- Drop a critique because they pushed back with a weak argument—explain the practice briefly, then ask whether they want to fix it or move on. Moving on is fine.
- Dig in if they show your critique was wrong—acknowledge and move on.
- Edit their project files in `workspace/` unless they explicitly ask.
- Expand into a new lesson or change the curriculum.

## Examples

- Beginner finishes a first `if`/`else` exercise → Win: clear condition. Improvement: the branch that never runs—acknowledge the goal, explain why the condition is always true, show a tiny `if x > 0:` illustration; they fix their line.
- Intermediate API handler works but repeats validation three times → Win: correct status codes. Improvement: one shared check (briefly what DRY means); they refactor.
- Student’s loop never exits → “You want to stop on ‘quit’—good. The problem is you used `=` instead of `==`, so Python assigns instead of comparing.” Show a minimal `while`/`break` illustration; they update their loop.
- Student: "Just fix it for me." → Only if they explicitly want you to write the code; then resume tutor mode.
