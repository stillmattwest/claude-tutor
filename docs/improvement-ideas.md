# Improvement ideas (backlog)

Maintainer notes on where `claude-tutor` could go next. Not student-facing.
Rough priority order within each tier.

---

## Tier 1 — highest leverage (pedagogy)

### 1. Spaced retrieval / anti-forgetting — ✅ done

The system taught forward but never backward: once a Skills-table row was
`mastered` it was never revisited, `check-understanding` only covered the current
lesson. Added the `review` skill (auto warm-up + `/review`), per-skill spacing
columns (`Last reviewed`, `Review` bucket `soon`/`near`/`far`/`retired`) on the
Skills table, and an append-only `.data/SESSIONS.md` for long-gap detection.

Possible follow-ups: tune bucket thresholds against real usage; add a
lightweight "recall streak" signal; let `/review` target a whole past section.

### 2. Debugging as a first-class taught skill

`stuck` (hint ladder) and `tutor-review`'s "explain why it failed" are reactive.
The *methodology* — read the error, form a hypothesis, bisect, minimal repro,
rubber-duck, use a debugger instead of prints — is never taught. This is the
skill that separates self-taught devs who finish from those who quit.

- Option A: require `curriculum` to include an explicit early debugging lesson.
- Option B: a `debug` coaching skill invoked (instead of plain `stuck`) whenever
  there's a real stack trace, walking the student through the process rather than
  toward the answer.

### 3. Session continuity / longitudinal signal

`.data/SESSIONS.md` now exists (minimal, for `review`). Grow it into a real
picture the tutor acts on: "shaky on async across three sessions — change
approach," "two-week gap — warm up harder."

Clean mid-lesson re-entry is now done: `teach-lesson` authors a frozen lesson
plan under `.data/.lessons/` on first delivery (see the `lesson-plan-format`
skill) and, on resume, reloads it and picks up from its `## Progress` →
`Resume at:` pointer (part-level) instead of regenerating a different version of
the lesson. `complete-lesson` marks the plan `complete`; `adjust-curriculum`
deletes stale non-complete plans; `mastertrack/complete-step.md` archives them.

Possible follow-ups: cross-session pattern detection (the "shaky across three
sessions" signal above); a student-facing progress line.

---

## Tier 2 — protect what works (engineering)

### 4. Eval harness — 🚧 in progress

Custom Python harness landed in `evals/` — see `evals/README.md`. Two layers:
static lint (frontmatter, name/dir, dangling refs, links, README drift; free) and
behavioural scenarios driving headless `claude -p` in sandboxed fixtures with
file-state + transcript + LLM-judge assertions. It ships 10 scenarios (5 in the
`--fast` CI subset) and a GitHub Actions workflow. `claude plugin eval` was set
aside — early-access, undocumented interface, needs plugin structure first (#5);
the behavioural runner is kept swappable.

Follow-ups: add the `section-end` fixture + scenarios that use it; tune judge
thresholds against real run data; revisit `claude plugin eval` after #5.

### 5. Package as a Claude Code plugin

Currently "clone this repo." A plugin makes it distributable, versionable, and
separable from the student's own work.

### 6. Decouple tutor scaffolding from student work

`.claude/`, `curriculum/`, `.data/` and `workspace/` all live in one repo the
student also commits to — hence the README's awkward "run `git init` inside
`workspace/`" caveat, and `curriculum/tracks/` bloat over time. Options: student
work in its own repo; tutor state under `~/.claude/` or a sibling dir;
`workspace/` as a separate repo or submodule.

---

## Tier 3 — depth where the content model is thin

### 7. Artifact-based assessment gates

`mastered` vs `shaky` is the model's read of "how independently they finished" —
soft. Single courses have no hard checkpoint. Let `section-review` require a
small from-scratch build with no hints as the gate, and record the result — the
way mastertrack milestones already work.

### 8. Prerequisite graph

Lessons chain linearly (section end = next start), but skills form a DAG. A
`depends-on: [1.2, 2.4]` field per lesson would let the tutor proactively shore
up a shaky prereq before teaching, and let `adjust-curriculum` reason about what's
safe to skip. The `review` skill currently *infers* prereqs from the lesson's
Start point text — it would use a real graph directly if one existed.

### 9. Author-supplied stack opinion packs

The "senior-correct path" bar leans entirely on model priors — fine for
mainstream Python/web, unreliable for Rust/Go/data/mobile/embedded. Add curated
opinion files (`references/stacks/*.md`) that `curriculum` consults, so the
author's actual taste is encoded rather than guessed.

### 10. Curriculum design checklists

"Introduce best practices when they first matter" is easy for the model to skip.
A hard list in `curriculum` ("every web course MUST cover: validation, auth
basics, a11y, deploy") enforces it.

### 11. Teach reading code / reading docs

Beginners can write from a blank page (with help) but freeze when dropped into an
existing codebase or the official docs. Nothing here teaches navigating
unfamiliar code or real documentation — a natural fit given the "works inside an
IDE" pitch.

---

## Quick wins

- **Student-facing progress line** — `CURRICULUM.md` has `# Current lesson:` but
  no "you are 12/40 lessons, 3 sections done" summary for motivation. Cheap to
  generate.
- **`workspace/` layout convention** — enforce `workspace/NN-section/N.N-lesson/`
  in `teach-lesson`; it gets messy across a long course.
- **Pin the `tutor-review` ceiling** (beginner/intermediate/advanced) in
  `STUDENT.md` instead of re-inferring it from soft signals every review.
