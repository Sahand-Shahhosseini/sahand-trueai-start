"""Core utilities for the Sahand SAT solver."""

from __future__ import annotations

import itertools
from typing import Dict, Iterable, List


class SahandSATCore:
    """Basic SAT solver with brute-force search."""

    def __init__(
        self,
        clauses: Iterable[Iterable[int]] | None = None,
        weights: Dict[int, float] | None = None,
    ) -> None:
        self.clauses: List[List[int]] = [list(c) for c in clauses] if clauses else []
        self.weights: Dict[int, float] = weights or {}
        self.variables = sorted({abs(l) for c in self.clauses for l in c})

    # ----- helpers -----
    def is_satisfied(self, assignment: Dict[int, bool]) -> bool:
        return all(
            any(
                (lit > 0 and assignment.get(abs(lit), False))
                or (lit < 0 and not assignment.get(abs(lit), False))
                for lit in clause
            )
            for clause in self.clauses
        )

    def cost(self, assignment: Dict[int, bool]) -> float:
        return sum(
            self.weights.get(v, 0.0) for v in self.variables if assignment.get(v, False)
        )

    # ----- solving -----
    def solve_bruteforce(self, verbose: bool = False) -> Dict:
        best, best_a = float("inf"), None
        for i, bits in enumerate(itertools.product([0, 1], repeat=len(self.variables))):
            assignment = {v: bool(bits[j]) for j, v in enumerate(self.variables)}
            if self.is_satisfied(assignment):
                c = self.cost(assignment)
                if c < best:
                    best, best_a = c, assignment.copy()
            if verbose and i % 1000 == 0:
                print(f"BF checked {i}")
        return {"assignment": best_a, "min_weight": best}
