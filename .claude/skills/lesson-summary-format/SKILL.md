---
name: lesson-summary-format
description: Lesson summary template for files under curriculum/lesson_summaries/. Use when creating or editing a lesson summary (typically from the complete-lesson skill).
---

# Lesson Summary Format

When creating or editing files under `curriculum/lesson_summaries/`, use this structure:

```markdown
# N.N Lesson title

## Concepts

- ...

## Commands / APIs

- ...

## What you built

- ...

## Open questions

- ...
```

Omit **Open questions** if there are none. Keep the summary short enough to skim later.

For a **short course** (`curriculum/CURRICULUM.md` has `**Type:** short course`) the file is flat — `curriculum/lesson_summaries/N-lesson-slug.md`, no section folder — and the heading is `# N Lesson title`.
