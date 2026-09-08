---
name: teach-lesson
description: Delivers the current curriculum lesson with explain-show-practice flow. Use when teaching the current lesson, starting a lesson, or continuing lesson work from curriculum/CURRICULUM.md.
---

# Teach Lesson

## Instructions

1. If `curriculum/MASTERTRACK.md` exists, check `.data/MASTERTRACK.md` and `.data/IN_MASTERTRACK_CURRICULUM` (missing = `off`) — reuse if already loaded this session, else read them together. If the current item is a milestone, capstone, or pause, **stop** — follow the `mastertrack` skill (`projects.md` or wait). Do not teach from `CURRICULUM.md`. If there is no map, ignore this check. Use `.data/STUDENT.md` and `.data/SESSIONS.md` (already read at session start; follow `student-profile` for updates) and pick up any **Resume** note from the last row. Note the **current lesson** in `curriculum/CURRICULUM.md` (title, start point, end goal). If the file has `**Type:** short course`, it has no sections and lesson IDs are `1`–`5`; there is no section-review, and `complete-lesson` handles the end of the course. Everything else here is unchanged — short-course lessons run the same flow and the same "split into parts" rule (a slightly longer lesson gets *more* parts, not a single dump). State the end goal in one sentence so the student knows what “done” looks like. Use their name. Skip or compress explanation for Skills-table rows with status `mastered`; spend more care on `shaky` rows and **Growth areas** when this lesson touches them.
2. **Load or author the saved lesson plan** (a file step — nothing is shown to the student yet). Compute the plan path for the current lesson: `.data/.lessons/<NN-section-slug>/<N.N-lesson-slug>.md` (same slugs as the lesson summary; for a **short course** the path is flat — `.data/.lessons/<N-lesson-slug>.md`). Follow the `lesson-plan-format` skill for the file shape.
   - **Plan exists.** Compare its `Built from end goal:` line to the current lesson's end goal in `curriculum/CURRICULUM.md`. If they differ, the plan is **stale** — say the lesson was updated since they last saw it, re-author the file (new `Generated:` date, `Progress` reset to `Part 1`), and deliver it fresh below. Otherwise **do not regenerate it**: load it and read `## Progress` → `Resume at:` — that is where step 4 picks up. Deliver from the plan's **saved** Orient, Show examples, and Exercise; do not invent new ones. If `Status:` is already `complete`, reuse the plan as a re-teach without rewriting it.
   - **No plan.** Author the full plan now — Orient, parts with their Show examples and Checks, Exercise, Code-review focus — following `lesson-plan-format` and the two rule sections below. Write the file with `Status: in progress`, every `## Progress` item unchecked, `Resume at: Part 1`.
3. **Warm-up.** Run the `review` skill first if earlier skills are due (Skills-table `Review` buckets, or a gap since the last `.data/SESSIONS.md` row). Keep it to 2–4 questions and let the student skip it — unless a due skill is a prerequisite for this lesson and comes back shaky, then shore it up before teaching. Start or update today's row in `.data/SESSIONS.md` (per `session-log-format`).
4. Deliver the lesson from the plan, following the flow below. **Start at the plan's `Resume at:` point**, not at Orient — on a resume, give a one-line recap of the finished parts, then continue. As each part's Check passes, tick it in the plan's `## Progress` and move `Resume at:` to the next part; do the same after the exercise and after code review (bookkeeping — do it without being asked).

   **Orient** — What is new in this lesson vs review from earlier lessons.

   **Explain + show** — Introduce new ideas in plain language, then **show a short example in chat** for every new piece of syntax the exercise will require (see rules below). **Deliver in parts** if the lesson is complex—do not dump everything at once.

   **Check understanding** — Ask the student to explain back in their own words before the main exercise (and between parts when the lesson is long).

   **Practice** — Give an exercise **they** type in `workspace/`. It should reach the lesson end goal using only what this lesson (and prior lessons) already taught or showed.

   **Code review** — Use the `tutor-review` skill on their work. Let them fix the one improvement you name.

   **Close** — When the end goal is met, follow `complete-lesson`. If blocked during practice, use `stuck`.

5. Match depth and vocabulary to `.data/STUDENT.md` (and prior lesson summaries). Stay encouraging and welcoming.

## Split complex lessons into parts (required)

This is what the saved lesson plan's `## Part N` sections capture — author them
this way, then deliver from them.

If a lesson has several new ideas or a long example, **split it into manageable parts**. Do not write a wall of text or hundreds of lines of explanation/code in one message.

Label each part for the student using the lesson id, e.g. **Lesson 2.1 Part 1**, **Lesson 2.1 Part 2**—not “Chunk 1.”

For each part:

1. **One focus** — e.g. one concept, one syntax shape, or one small example (roughly a screenful of chat, not a novel).
2. **Show** — minimal example for what that part introduces.
3. **Check** — quick teach-back or “what does this line do?” before the next part.
4. **Advance when ready** — only move to the next part or the exercise when they follow the current piece. If they are shaky, re-show or simplify; do not pile on.

The full lesson end goal can still span multiple parts and exercises in one session; the student should never feel they were expected to absorb everything in a single dump.

## Show before you expect (required)

**Never ask the student to write syntax, APIs, or patterns they have not been shown in this lesson or a prior one.**

Before any exercise that uses something **new in this lesson**, show a minimal example in chat and briefly say what the important lines do:

- **Language basics** — e.g. first class: show a constructor/`__init__` (or equivalent) before asking them to write a class.
- **Data structures** — e.g. first dict/list comprehension: show one small example before they build their own.
- **Framework / engine / library** — e.g. first FastAPI route, first React hook, first SQLAlchemy model: show the shape of the call/decorator/method before they reproduce it.
- **CLI or tool syntax** — show the command pattern once before they run a variant.

### Point to what they already have

If the syntax or pattern was **already taught and practiced** in an earlier lesson or exists in **their project**, you do not need to show a fresh chat example every time. Instead:

- Point them to the **earlier lesson summary** (`curriculum/lesson_summaries/...`) or the **file and spot** in `workspace/` where they wrote it before.
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
- Do not create or edit project files for them unless they explicitly ask. When they ask, put files in `workspace/`.
- Do not skip teach-back to get to coding faster.

## Do not

- Do not dump an entire complex lesson in one message—use parts and checks between them.
- Use analogies as they can be confusing. Just explain the concept you are teaching in plain language.
- Teach the next lesson or section before the current end goal is met.
- Assign exercises that require unread docs or undiscovered syntax.
- Dump a full solution when they are stuck—use `stuck` instead.
- Treat frameworks or engine features as black boxes: explain what the tool is and why it is shaped that way when first shown.
- Re-author a saved lesson plan that is still `in progress`, or swap its examples / exercise for new ones on resume. Only its `## Progress` block and `Status` change until the lesson is done. Route lesson content changes through `adjust-curriculum`.

## Examples

- Lesson 1.5 introduces Python classes → **Lesson 1.5 Part 1**: tiny class + `__init__` + what `self` is; check. **Part 2**: one method; check. Then exercise: add a field and method.
- Later lesson needs another class → Point to their earlier class/`__init__` in `workspace/` or a lesson summary; ask them to adapt it. Re-show only if they ask or are stuck.
- **Lesson 2.1 Part 1** introduces FastAPI POST → show `@app.post(...)` and body model; check. Then exercise: second endpoint same pattern.
- Student asks to start lesson 2.3 → Orient with the end goal, show only what 2.3 adds new, then practice.
