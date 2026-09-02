# Archive the live course before replacing it

Follow this **before** `curriculum`, `short-course`, or `mastertrack` writes a new
plan over an existing one. It protects work the student may still want.

## Steps

1. If `curriculum/CURRICULUM.md` does **not** exist, skip this file — there is
   nothing to replace. Continue with the design.
2. If it exists, **stop and warn.** Name the live course (its title and the
   `# Current lesson:` line) and tell the student that starting a new plan will
   set the current one aside. Ask them to confirm.
   - If they would rather keep the current course, do **not** redesign. For pace,
     skips, or a capstone change, use `adjust-curriculum`. Only continue here when
     they clearly want a different plan.
   - If `curriculum/MASTERTRACK.md` exists and `.data/IN_MASTERTRACK_CURRICULUM`
     is `on`, the live course is a **mapped step** — do not archive it here. Route
     to `adjust-mastertrack` (topic or order change) or `adjust-curriculum` (pace
     inside the step).
3. On confirmation, archive the **whole course** into a dated folder:
   - Make `curriculum/archive/YYYY-MM-DD/` using today's date. If that folder
     already exists, append `-2`, `-3`, … so nothing is overwritten.
   - Move `curriculum/CURRICULUM.md` and the entire
     `curriculum/lesson_summaries/` directory into it. Also move
     `.data/.lessons/` (the saved lesson plans) into it if that folder exists —
     every plan is against the course being replaced.
   - Recreate an empty `curriculum/lesson_summaries/` for the new plan.
     `.data/.lessons/` does not need recreating — `teach-lesson` makes it on the
     first lesson.
   - Otherwise do **not** touch `.data/` here. The design skill rewrites the
     Skills table itself via `student-profile` (keeping name, strengths, and
     growth areas).
4. Tell the student where the old course was archived (they can still open it),
   then continue with the new design.

## Do not

- Overwrite or delete an existing `CURRICULUM.md` without archiving it first.
- Archive a mapped mastertrack step — send those to `adjust-mastertrack`.
- Copy the old Skills table forward wholesale; the design skill handles the
  profile.
