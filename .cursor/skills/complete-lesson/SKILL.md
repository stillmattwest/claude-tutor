---
name: complete-lesson
description: Writes the lesson summary and advances the current-lesson pointer when a lesson end goal is met. Use when the student has met the current lesson end goal or the tutor confirms the lesson is complete.
---

# Complete Lesson

## Instructions

1. Confirm the current lesson’s **end goal** in `CURRICULUM.md` is met. If not, stop and say what is still missing.
2. Create the summary file (create the section folder if needed):

   `lesson_summaries/NN-section-slug/N.N-lesson-slug.md`

   Example: `lesson_summaries/01-your-computer-as-a-workshop/1.1-files-folders-and-the-terminal.md`

3. Write the summary with these headings:

   - **Concepts** — ideas from the lesson
   - **Commands / APIs** — commands, functions, or APIs they used
   - **What you built** — files or artifacts they created
   - **Open questions** — optional; omit the section if none

4. Update the `# Current lesson:` line at the top of `CURRICULUM.md` to the next lesson. If this was the last lesson in a section and the section end goal is met, follow the `section-review` skill next (or point the student there). If the course is finished, set the current-lesson line to a clear “complete” note.
5. Do this bookkeeping without waiting to be asked. Then tell the student the lesson is done and what the next lesson is.

## Do not

- Advance if the end goal is not met.
- Overwrite an existing summary unless correcting a mistake the student agrees with.
- Start teaching the next lesson in the same breath as a long dump — name it, then wait for them to begin.
