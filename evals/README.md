# claude-tutor eval harness

Regression protection for the skills. Two layers:

- **Layer 1 — static lint** (`lint.py`): frontmatter validity, `name`/directory
  match, dangling skill references, broken relative links, leftover Cursor
  artifacts, README/skill drift, step renumbering slips. No API calls; runs in
  milliseconds.
- **Layer 2 — behavioural scenarios** (`harness.py` + `scenarios/`): compose a
  throwaway repo (the live `.claude/` + `CLAUDE.md` over a fixture's student
  state), play scripted student turns through headless `claude -p`, then assert
  on the files written and the transcript.

## Running

```bash
python evals/run.py --lint                     # Layer 1 only — free, fast
python evals/run.py --fast                       # lint + the CI subset (~4 scenarios)
python evals/run.py --behavioral                 # every scenario
python evals/run.py --scenario NAME [--scenario NAME ...]
python evals/run.py --scenario NAME --runs 1 --keep   # debug one run, keep the sandbox
python evals/run.py                              # lint + all behavioural
```

Requires Python 3.10+ and the `claude` CLI on `PATH`. Behavioural runs need
`ANTHROPIC_API_KEY` in the environment and cost real money (roughly a few dollars
for the full suite; `--lint` is free). Results are written to
`evals/report.json`; failed runs leave their sandbox under `evals/.work/` with a
`_transcript.json` for inspection.

## How a scenario works

A `Scenario` (see `harness.py`) is:

```python
Scenario(
    name="curriculum_design_does_not_teach",
    fixture="empty",                 # evals/fixtures/<name>/ — student state only
    turns=[ "student message 1", "student message 2", ... ],
    check=check_fn,                  # (workdir: Path, transcript) -> Iterable[Result]
    runs=2, need=2,                 # run N times, require k passes (flake guard)
    fast=True,                       # part of the --fast / CI subset
)
```

`check_fn` yields `Result(label, ok, detail)` values. Prefer **file-state**
assertions (`file_exists`, `file_matches`, `file_unchanged`, `glob_exists`) —
they are deterministic. Use `text_has` / `text_lacks` against `transcript.turn(i)`
for coarse transcript checks, and `judge(rubric, sample)` (a separate graded
`claude -p` call) only for tone/pedagogy questions structure can't capture.

Fixtures contain only `curriculum/`, `.data/`, and `workspace/` — never a copy of
the skills — so they don't rot when a skill changes.

## Adding a scenario

1. Pick or add a fixture under `evals/fixtures/`.
2. Add a `Scenario` to the relevant module in `evals/scenarios/`
   (`curriculum.py`, `lessons.py`, `mastertrack.py`).
3. Iterate with `--scenario NAME --runs 1 --keep` and read the kept
   `_transcript.json`.
4. Prove it has teeth: temporarily break the skill instruction it guards and
   confirm the scenario fails, then revert.

## Notes / known constraints

- Slash commands (`/curriculum`, `/review`) work under `claude -p`; multi-turn
  uses `--continue` to resume the sandbox's session.
- The tutor legitimately needs enough turns to clear intake and the
  infer-scope forks — front-load every intake fact in one student turn so the
  conversation doesn't branch.
- The behavioural runner is intentionally swappable: if claude-tutor becomes a
  plugin, `claude plugin eval` / `/skill-doctor` can replace or augment it.
