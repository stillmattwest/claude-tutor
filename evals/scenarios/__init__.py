"""Scenario registry. `SCENARIOS` is the full v1 suite."""

from __future__ import annotations

from harness import Scenario

from . import curriculum, lessons, mastertrack

SCENARIOS: list[Scenario] = [
    *curriculum.SCENARIOS,
    *lessons.SCENARIOS,
    *mastertrack.SCENARIOS,
]

FAST: list[Scenario] = [s for s in SCENARIOS if s.fast]

by_name = {s.name: s for s in SCENARIOS}
