"""Knapsack-style optimization using the Sahand SAT solver."""

from __future__ import annotations

import json
from typing import Dict

from .SahandSAT_Extended import SahandSATExtended


class SahandKnapsack:
    def __init__(self, problem: str | Dict) -> None:
        if isinstance(problem, str):
            with open(problem, "r") as f:
                problem = json.load(f)
        weights = {int(k): float(v) for k, v in problem.get("weights", {}).items()}
        self.solver = SahandSATExtended(
            clauses=problem.get("clauses"),
            weights=weights,
        )

    def optimize(self, verbose: bool = False) -> Dict:
        return self.solver.solve(verbose)

    def export(self, path: str) -> None:
        if not hasattr(self.solver, "solution"):
            result = self.optimize()
        else:
            result = self.solver.solution
        self.solver.save_json(path, result)
