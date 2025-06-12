5tek9r-codex/save-sahandsat-solver-code-to-file
=======
3aot3p-codex/save-sahandsat-solver-code-to-file
=======
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

main
main
from sat_solver.SahandSAT_PySAT import SahandSAT


def test_sahand_sat_pysat_min_weight():
    clauses = [[1, 2], [-1, 2]]
    weights = {1: 1.0, 2: 0.5}
    solver = SahandSAT(clauses=clauses, weights=weights)
    result = solver.solve()
    assert result["min_weight"] == 0.5
    assert result["assignment"][2] is True
    assert result["assignment"][1] is False


def test_sahand_sat_pysat_method():
    clauses = [[1], [-1, 2]]
    solver = SahandSAT(clauses=clauses)
    result = solver.solve()
    assert result["method"] in {"bruteforce", "pysat"}
