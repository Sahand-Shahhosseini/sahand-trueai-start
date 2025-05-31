import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sstai.core.sahand_sat import SahandSAT


def test_sahand_sat_solver_min_weight():
    clauses = [[1, 2], [-1, 2]]
    weights = {1: 1.0, 2: 0.5}
    solver = SahandSAT(clauses=clauses, weights=weights)
    result = solver.solve()
    assert result["min_weight"] == 0.5
    assert result["assignment"][2] is True
    assert result["assignment"][1] is False
