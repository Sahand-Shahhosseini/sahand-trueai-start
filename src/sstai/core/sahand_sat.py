import itertools
import json
import time
from typing import Dict, Iterable, List, Union

try:
    from pysat.formula import CNF
    from pysat.solvers import Glucose3

    HAS_PYSAT = True
except ImportError:  # pragma: no cover - optional dependency
    HAS_PYSAT = False


class SahandSAT:
    """Simple CNF SAT solver with weight-based optimization."""

    def __init__(
        self,
        clauses: Iterable[Iterable[int]] | None = None,
        weights: Dict[int, float] | None = None,
    ):
        self.clauses: List[List[int]] = [list(c) for c in clauses] if clauses else []
        self.weights: Dict[int, float] = weights or {}
        self.variables = sorted({abs(l) for c in self.clauses for l in c})
        self.solution: Dict[str, Union[float, dict]] | None = None

    def load_from_json(self, data: Union[str, Dict]) -> None:
        """Load clauses and weights from a JSON filepath or object."""
        if isinstance(data, str):
            with open(data, "r") as f:
                data = json.load(f)
        self.clauses = [list(cl) for cl in data.get("clauses", [])]
        self.weights = {int(k): float(v) for k, v in data.get("weights", {}).items()}
        self.variables = sorted({abs(l) for c in self.clauses for l in c})

    def is_satisfied(self, assignment: Dict[int, bool]) -> bool:
        """Return True if all clauses are satisfied under the assignment."""
        for clause in self.clauses:
            if not any(
                (lit > 0 and assignment.get(abs(lit), False))
                or (lit < 0 and not assignment.get(abs(lit), False))
                for lit in clause
            ):
                return False
        return True

    def total_weight(self, assignment: Dict[int, bool]) -> float:
        """Compute the sum of weights for variables set to True."""
        return sum(
            self.weights.get(v, 0.0) for v in self.variables if assignment.get(v, False)
        )

    def solve(self, verbose: bool = False) -> Dict:
        """Solve the SAT instance using PySAT if available."""
        if HAS_PYSAT:
            return self._solve_pysat(verbose)
        return self._solve_bruteforce(verbose)

    def _solve_bruteforce(self, verbose: bool = False) -> Dict:
        min_weight = float("inf")
        best_assignment: Dict[int, bool] | None = None
        start = time.time()
        total = 2 ** len(self.variables)

        for idx, bits in enumerate(
            itertools.product([False, True], repeat=len(self.variables))
        ):
            assignment = {v: bits[i] for i, v in enumerate(self.variables)}
            if self.is_satisfied(assignment):
                w = self.total_weight(assignment)
                if w < min_weight:
                    min_weight = w
                    best_assignment = assignment.copy()
            if verbose and idx % 100 == 0:
                print(f"Checked {idx}/{total} assignments...")

        elapsed = time.time() - start
        self.solution = {
            "min_weight": min_weight,
            "assignment": best_assignment,
            "vars": self.variables,
            "clause_count": len(self.clauses),
            "time_seconds": elapsed,
            "method": "bruteforce",
        }
        return self.solution

    def _solve_pysat(self, verbose: bool = False) -> Dict:
        start = time.time()
        cnf = CNF(from_clauses=self.clauses)
        best, best_a = float("inf"), None
        with Glucose3(bootstrap_with=cnf) as solver:
            while solver.solve():
                model = solver.get_model()
                a = {abs(v): v > 0 for v in model}
                cost = self.total_weight(a)
                if cost < best:
                    best, best_a = cost, a.copy()
                solver.add_clause([-v if a[abs(v)] else v for v in self.variables])

        elapsed = time.time() - start
        self.solution = {
            "min_weight": best,
            "assignment": best_a,
            "vars": self.variables,
            "clause_count": len(self.clauses),
            "time_seconds": elapsed,
            "method": "pysat",
        }
        return self.solution

    def export_to_json(self, filepath: str, include_solution: bool = False) -> None:
        """Write problem definition and optional solution to a JSON file."""
        data = {"clauses": self.clauses, "weights": self.weights}
        if include_solution:
            if self.solution is None:
                self.solve()
            data.update(
                {
                    "solution": self.solution["assignment"],
                    "min_weight": self.solution["min_weight"],
                    "method": self.solution.get("method", "bruteforce"),
                }
            )
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)

    def symbolic_signature(self) -> Dict[str, float]:
        """Return a symbolic summary of the SAT instance."""
        literal_count = sum(len(c) for c in self.clauses)
        var_count = len(self.variables)
        entropy_sum = sum(self.weights.values())
        return {
            "literal_count": literal_count,
            "variable_count": var_count,
            "entropy_weight_sum": entropy_sum,
            "clauses": len(self.clauses),
            "density": len(self.clauses) / max(1, var_count),
        }

    def print_summary(self) -> None:
        sig = self.symbolic_signature()
        print("\U0001f4d8 SahandSAT Instance Summary")
        print(f" - Variables: {sig['variable_count']}")
        print(f" - Clauses: {sig['clauses']}")
        print(f" - Total Entropy Weight: {sig['entropy_weight_sum']:.3f}")
        print(f" - Density: {sig['density']:.2f}")
        print(f" - Literals (total): {sig['literal_count']}")
