#!/usr/bin/env python3
"""Entry point for the claude-tutor eval harness.

    python evals/run.py --lint                 # static checks only (free, fast)
    python evals/run.py --behavioral           # every behavioural scenario
    python evals/run.py --fast                  # lint + the CI subset
    python evals/run.py --scenario NAME [...]   # named scenarios
    python evals/run.py                         # lint + all behavioural

Exit code is non-zero if anything failed.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from common import ScenarioReport, print_report  # noqa: E402
from harness import DEFAULT_MODEL, run_scenario  # noqa: E402
from lint import run_lint  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lint", action="store_true", help="run static checks")
    ap.add_argument("--behavioral", action="store_true", help="run all behavioural scenarios")
    ap.add_argument("--fast", action="store_true", help="lint + the fast scenario subset")
    ap.add_argument("--scenario", action="append", default=[], metavar="NAME", help="run named scenario(s)")
    ap.add_argument("--runs", type=int, default=None, help="override runs-per-scenario")
    ap.add_argument("--model", default=DEFAULT_MODEL, help="model to run the tutor as")
    ap.add_argument("--keep", action="store_true", help="keep sandbox dirs even on pass")
    ap.add_argument("--json", type=Path, default=HERE / "report.json", help="report output path")
    args = ap.parse_args()

    from scenarios import FAST, SCENARIOS, by_name

    do_lint = args.lint or args.fast or not (args.behavioral or args.scenario)
    if args.scenario:
        chosen = [by_name[n] for n in args.scenario if n in by_name]
        unknown = [n for n in args.scenario if n not in by_name]
        for n in unknown:
            print(f"unknown scenario: {n}", file=sys.stderr)
        if unknown and not chosen:
            return 2
    elif args.fast:
        chosen = FAST
    elif args.behavioral or not args.lint:
        chosen = SCENARIOS
    else:
        chosen = []

    started = time.time()
    lint_results = run_lint() if do_lint else []
    reports: list[ScenarioReport] = []
    for scenario in chosen:
        n = scenario.runs if args.runs is None else args.runs
        print(f"... running {scenario.name} ({n} run(s))", flush=True)
        report = run_scenario(scenario, model=args.model, runs=args.runs, keep=args.keep)
        verdict = "PASS" if report.ok else "FAIL"
        print(f"    -> {verdict}  {report.passed_runs}/{report.runs}  ${report.cost_usd:.2f}", flush=True)
        reports.append(report)

    print_report(reports, lint_results)

    lint_ok = all(r.ok for r in lint_results)
    beh_ok = all(r.ok for r in reports)
    total_cost = sum(r.cost_usd for r in reports)
    elapsed = time.time() - started
    print(
        f"\nlint: {'PASS' if lint_ok else 'FAIL'}   "
        f"behavioural: {sum(r.ok for r in reports)}/{len(reports)} passed   "
        f"${total_cost:.2f}   {elapsed:.0f}s"
    )

    args.json.write_text(
        json.dumps(
            {
                "lint": [r.__dict__ for r in lint_results],
                "scenarios": [
                    {
                        "name": r.name,
                        "ok": r.ok,
                        "passed_runs": r.passed_runs,
                        "runs": r.runs,
                        "need": r.need,
                        "error": r.error,
                        "cost_usd": r.cost_usd,
                        "per_run": [[res.__dict__ for res in run] for run in r.per_run],
                    }
                    for r in reports
                ],
                "total_cost_usd": total_cost,
                "elapsed_s": elapsed,
            },
            indent=2,
        )
    )
    return 0 if lint_ok and beh_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
