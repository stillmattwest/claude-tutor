---
name: section-review
description: End-of-section checkpoint against the section end goal, then advance to the next section. Use when a section end goal is met or the student asks for a section review.
---

# Section Review

## Instructions

1. Read the finished section’s **end goal** in `CURRICULUM.md`.
2. Check the student against that goal (short teach-back or inspect what they built). List gaps in plain language.
3. If gaps remain, give one focused remediation exercise; do **not** advance until the section end goal is met (unless the student explicitly wants to move on knowing the gap).
4. If the last lesson of the section is complete but `complete-lesson` has not run yet, follow `complete-lesson` first.
5. When the section end goal is met:
   - Briefly celebrate and summarize what the section unlocked.
   - Set `# Current lesson:` to the first lesson of the next section (if `complete-lesson` did not already).
   - Follow `student-profile`: update each Skills-table row in this section (`mastered` / `shaky`) and prune notes that no longer apply.
   - Tell the student the next section’s start point and first lesson title.
6. Optional: one short critique of their capstone-so-far or section project — strengths and one improvement — only if they built something reviewable.

## Do not

- Redesign the curriculum (use `adjust-curriculum` or `curriculum`).
- Skip naming concrete gaps.
- Jump multiple sections ahead.

## Examples

- Student finishes section 1 end goal → Confirm goal, note any weak spot, point at `2.1` as current lesson.
- Student: "Review section 2 with me." → Quiz against section 2 end goal; remediate or advance accordingly.
