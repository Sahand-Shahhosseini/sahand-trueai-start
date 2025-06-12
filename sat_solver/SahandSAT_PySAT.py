"""Minimal SAT solver with optional PySAT backend."""

from __future__ import annotations

import itertools
import json
import time
from typing import Dict, Iterable, List, Optional

try:  # pragma: no cover - optional dependency
    from pysat.formula import CNF
    from pysat.solvers import Glucose3

    HAS_PYSAT = True
except ImportError:  # pragma: no cover - optional dependency
    HAS_PYSAT = False


class SahandSAT:
    """Lightweight solver supporting optional weight minimization."""

    def __init__(
        self,
        clauses: Optional[Iterable[Iterable[int]]] = None,
        weights: Optional[Dict[int, float]] = None,
    ) -> None:
        self.clauses: List[List[int]] = [list(c) for c in clauses] if clauses else []
        self.weights: Dict[int, float] = weights or {}
        self.vars: List[int] = sorted({abs(l) for c in self.clauses for l in c})

    # ---------- helpers ----------
    def _satisfied(self, a: Dict[int, bool]) -> bool:
        return all(
            any(
                (lit > 0 and a.get(abs(lit), False))
                or (lit < 0 and not a.get(abs(lit), False))
                for lit in clause
            )
            for clause in self.clauses
        )

    def _cost(self, a: Dict[int, bool]) -> float:
        return sum(self.weights.get(v, 0.0) for v in self.vars if a.get(v, False))

    # ---------- solver ----------
    def solve(self, verbose: bool = False) -> Dict:
        return (
            self._solve_pysat(verbose) if HAS_PYSAT else self._solve_bruteforce(verbose)
        )

    def _solve_bruteforce(self, verbose: bool = False) -> Dict:
        best, best_a = float("inf"), None
        start = time.time()
        for i, bits in enumerate(itertools.product([0, 1], repeat=len(self.vars))):
            a = {v: bool(bits[j]) for j, v in enumerate(self.vars)}
            if self._satisfied(a):
                c = self._cost(a)
                if c < best:
                    best, best_a = c, a.copy()
            if verbose and i % 1000 == 0:
                print(f"BF {i} checked")
        return {
            "assignment": best_a,
            "min_weight": best,
            "method": "bruteforce",
            "time": time.time() - start,
        }

    def _solve_pysat(self, verbose: bool = False) -> Dict:
        start = time.time()
        cnf = CNF(from_clauses=self.clauses)
        best, best_a = float("inf"), None
        with Glucose3(bootstrap_with=cnf) as m:
            while m.solve():
                model = m.get_model()
                a = {abs(v): v > 0 for v in model}
                c = self._cost(a)
                if c < best:
                    best, best_a = c, a.copy()
                m.add_clause([-v if a[abs(v)] else v for v in self.vars])
        return {
            "assignment": best_a,
            "min_weight": best,
            "method": "pysat",
            "time": time.time() - start,
        }

    # ---------- IO ----------
    def load_json(self, path: str) -> None:
        with open(path, "r") as f:
            data = json.load(f)
        self.clauses = data.get("clauses", [])
        self.weights = {int(k): float(v) for k, v in data.get("weights", {}).items()}
        self.vars = sorted({abs(l) for c in self.clauses for l in c})

    def save_json(self, path: str, sol: Optional[Dict[int, bool]] = None) -> None:
        data = {"clauses": self.clauses, "weights": self.weights}
        if sol:
            data["solution"] = sol
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
