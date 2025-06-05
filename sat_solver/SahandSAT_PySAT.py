# SahandSAT with optional PySAT backend
import json
import time
import itertools

try:
    from pysat.formula import CNF
    from pysat.solvers import Glucose3

    HAS_PYSAT = True
except ImportError:
    HAS_PYSAT = False


class SahandSAT:
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
        return (
            self._solve_pysat(verbose) if HAS_PYSAT else self._solve_bruteforce(verbose)
        )

    def _solve_bruteforce(self, verbose):
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

    def _solve_pysat(self, verbose):
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
    def load_json(self, path):
        d = json.load(open(path))
        self.clauses, self.weights = d["clauses"], d["weights"]
        self.vars = sorted({abs(l) for c in self.clauses for l in c})

    def save_json(self, path, sol=None):
        d = {"clauses": self.clauses, "weights": self.weights}
        if sol:
            d["solution"] = sol
        json.dump(d, open(path, "w"), indent=2)
