<<<<<<s2wo86-codex/save-sahandsat-solver-code-to-file
=======
5tek9r-codex/save-sahandsat-solver-code-to-file
>>>>>>main
"""Minimal SAT solver with optional PySAT backend."""

from __future__ import annotations

import itertools
import json
import time
from typing import Dict, Iterable, List, Optional

try:  # pragma: no cover - optional dependency
<<<<<<s2wo86-codex/save-sahandsat-solver-code-to-file
=======
=======
# SahandSAT with optional PySAT backend
import json
import time
import itertools

try:
main
>>>>>>main
    from pysat.formula import CNF
    from pysat.solvers import Glucose3

    HAS_PYSAT = True
<<<<<<s2wo86-codex/save-sahandsat-solver-code-to-file
except ImportError:  # pragma: no cover - optional dependency
=======
5tek9r-codex/save-sahandsat-solver-code-to-file
except ImportError:  # pragma: no cover - optional dependency
=======
except ImportError:
main
>>>>>>main
    HAS_PYSAT = False


class SahandSAT:
<<<<<<s2wo86-codex/save-sahandsat-solver-code-to-file
=======
5tek9r-codex/save-sahandsat-solver-code-to-file
>>>>>>main
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
<<<<<<s2wo86-codex/save-sahandsat-solver-code-to-file
=======
=======
    def __init__(self, clauses=None, weights=None):
        self.clauses = clauses or []
        self.weights = weights or {}
        self.vars = sorted({abs(l) for c in self.clauses for l in c})

    # ---------- helpers ----------
    def _satisfied(self, a):
        return all(
            any((l > 0 and a[abs(l)]) or (l < 0 and not a[abs(l)]) for l in cl)
            for cl in self.clauses
        )

    def _cost(self, a):
        return sum(self.weights.get(v, 0) for v in self.vars if a[v])

    # ---------- solver ----------
    def solve(self, verbose=False):
main
>>>>>>main
        return (
            self._solve_pysat(verbose) if HAS_PYSAT else self._solve_bruteforce(verbose)
        )

<<<<<<s2wo86-codex/save-sahandsat-solver-code-to-file
    def _solve_bruteforce(self, verbose: bool = False) -> Dict:
=======
5tek9r-codex/save-sahandsat-solver-code-to-file
    def _solve_bruteforce(self, verbose: bool = False) -> Dict:
=======
    def _solve_bruteforce(self, verbose):
main
>>>>>>main
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

<<<<<<s2wo86-codex/save-sahandsat-solver-code-to-file
    def _solve_pysat(self, verbose: bool = False) -> Dict:
=======
5tek9r-codex/save-sahandsat-solver-code-to-file
    def _solve_pysat(self, verbose: bool = False) -> Dict:
=======
    def _solve_pysat(self, verbose):
main
>>>>>>main
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
<<<<<<s2wo86-codex/save-sahandsat-solver-code-to-file
=======
5tek9r-codex/save-sahandsat-solver-code-to-file
>>>>>>main
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
<<<<<<s2wo86-codex/save-sahandsat-solver-code-to-file
=======
=======
    def load_json(self, path):
        d = json.load(open(path))
        self.clauses, self.weights = d["clauses"], d["weights"]
        self.vars = sorted({abs(l) for c in self.clauses for l in c})

    def save_json(self, path, sol=None):
        d = {"clauses": self.clauses, "weights": self.weights}
        if sol:
            d["solution"] = sol
        json.dump(d, open(path, "w"), indent=2)
main
>>>>>>main
