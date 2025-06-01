"""Extended SAT solver with optional PySAT backend and JSON utilities."""

from __future__ import annotations

import json
import time
from typing import Dict, Iterable, List

from .SahandSAT_Core import SahandSATCore

try:  # pragma: no cover - optional dependency
    from pysat.formula import CNF
    from pysat.solvers import Glucose3

    HAS_PYSAT = True
except Exception:  # pragma: no cover - PySAT may be missing
    HAS_PYSAT = False


class SahandSATExtended(SahandSATCore):
    """Sahand SAT solver with convenient IO and PySAT acceleration."""

    def load_json(self, path_or_obj: str | Dict) -> None:
        if isinstance(path_or_obj, str):
            with open(path_or_obj, "r") as f:
                data = json.load(f)
        else:
            data = path_or_obj
        self.clauses = [list(c) for c in data.get("clauses", [])]
        self.weights = {int(k): float(v) for k, v in data.get("weights", {}).items()}
        self.variables = sorted({abs(l) for c in self.clauses for l in c})

    def save_json(self, path: str, solution: Dict | None = None) -> None:
        data = {"clauses": self.clauses, "weights": self.weights}
        if solution:
            data["solution"] = solution
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

    def solve(self, verbose: bool = False) -> Dict:
        if HAS_PYSAT:
            return self._solve_pysat(verbose)
        return self.solve_bruteforce(verbose)

    def _solve_pysat(self, verbose: bool = False) -> Dict:
        start = time.time()
        cnf = CNF(from_clauses=self.clauses)
        best, best_a = float("inf"), None
        with Glucose3(bootstrap_with=cnf) as solver:
            while solver.solve():
                model = solver.get_model()
                a = {abs(v): v > 0 for v in model}
                c = self.cost(a)
                if c < best:
                    best, best_a = c, a.copy()
                solver.add_clause([-v if a[abs(v)] else v for v in self.variables])
        return {
            "assignment": best_a,
            "min_weight": best,
            "method": "pysat",
            "time": time.time() - start,
        }

    def summary(self) -> Dict[str, int]:
        return {"variables": len(self.variables), "clauses": len(self.clauses)}
