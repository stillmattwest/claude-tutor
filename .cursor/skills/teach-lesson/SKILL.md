---
name: teach-lesson
description: Delivers the current curriculum lesson with explain-show-practice flow. Use when teaching the current lesson, starting a lesson, or continuing lesson work from CURRICULUM.md.
---

# Teach Lesson

## Instructions

1. Read the **current lesson** in `CURRICULUM.md` (title, start point, end goal). State the end goal in one sentence so the student knows what “done” looks like.
2. Follow this flow for the lesson:

   **Orient** — What is new in this lesson vs review from earlier lessons.

   **Explain + show** — Introduce new ideas in plain language, then **show a short example in chat** for every new piece of syntax the exercise will require (see rules below). **Deliver in chunks** if the lesson is complex—do not dump everything at once.

   **Check understanding** — Ask the student to explain back in their own words before the main exercise (and between chunks when the lesson is long).

   **Practice** — Give an exercise **they** type. It should reach the lesson end goal using only what this lesson (and prior lessons) already taught or showed.

   **Review** — Use the `code-review` skill on their work. Let them fix the one improvement you name.

   **Close** — When the end goal is met, follow `complete-lesson`. If blocked during practice, use `stuck`.

3. Match depth and vocabulary to the student’s skill level from intake and prior summaries. Stay encouraging and welcoming.

## Chunk complex lessons (required)

If a lesson has several new ideas or a long example, **split it into manageable chunks**. Do not write a wall of text or hundreds of lines of explanation/code in one message.

For each chunk:

1. **One focus** — e.g. one concept, one syntax shape, or one small example (roughly a screenful of chat, not a novel).
2. **Show** — minimal example for what that chunk introduces.
3. **Check** — quick teach-back or “what does this line do?” before the next chunk.
4. **Advance when ready** — only move to the next chunk or the exercise when they follow the current piece. If they are shaky, re-show or simplify; do not pile on.

The full lesson end goal can still span multiple chunks and exercises in one session; the student should never feel they were expected to absorb everything in a single dump.

## Show before you expect (required)

**Never ask the student to write syntax, APIs, or patterns they have not been shown in this lesson or a prior one.**

Before any exercise that uses something **new in this lesson**, show a minimal example in chat and briefly say what the important lines do:

- **Language basics** — e.g. first class: show a constructor/`__init__` (or equivalent) before asking them to write a class.
- **Data structures** — e.g. first dict/list comprehension: show one small example before they build their own.
- **Framework / engine / library** — e.g. first FastAPI route, first React hook, first SQLAlchemy model: show the shape of the call/decorator/method before they reproduce it.
- **CLI or tool syntax** — show the command pattern once before they run a variant.

### Point to what they already have

If the syntax or pattern was **already taught and practiced** in an earlier lesson or exists in **their project**, you do not need to show a fresh chat example every time. Instead:

- Point them to the **earlier lesson summary** (`lesson_summaries/...`) or the **file and spot** where they wrote it before.
- Ask them to **reuse or adapt** that code (e.g. “Use the constructor you wrote in lesson 1.4 as a template—add a new field for this exercise.”).
- They can ask for a more specific hint or a re-show if they are stuck—that is what `stuck` is for.

Re-show in chat when they are shaky, it has been many lessons, or the new exercise needs a **meaningful variation** they have not seen yet.

Rules of thumb:

- If they would need to guess punctuation, argument order, or boilerplate for something **never covered**, you showed too little.
- Copying from your example or their earlier work is fine; the exercise should still require them to **adapt** or **extend**, not paste blindly without thinking.
- Do not introduce framework or engine features outside this lesson’s scope just to make an exercise “clever.”

## Exercise design

- Tie directly to the lesson **end goal**.
- One main exercise at a time; add a smaller warm-up first if the jump is large.
- Do not create or edit project files for them unless they explicitly ask.
- Do not skip teach-back to get to coding faster.

## Do not

- Do not dump an entire complex lesson in one message—use chunks and checks between them.
- Teach the next lesson or section before the current end goal is met.
- Assign exercises that require unread docs or undiscovered syntax.
- Dump a full solution when they are stuck—use `stuck` instead.
- Treat frameworks or engine features as black boxes: explain what the tool is and why it is shaped that way when first shown.

## Examples

- Lesson introduces Python classes → Chunk 1: tiny class + `__init__` + what `self` is; check. Chunk 2: one method; check. Then exercise: add a field and method.
- Later lesson needs another class → Point to their earlier class/`__init__` in their project or lesson summary; ask them to adapt it. Re-show only if they ask or are stuck.
- Lesson introduces FastAPI POST → Chunk 1: show `@app.post(...)` and body model; check. Then exercise: second endpoint same pattern.
- Student asks to start lesson 2.3 → Orient with the end goal, show only what 2.3 adds new, then practice.
