import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sstai.core.SahandSAT_Core import SahandSAT
from sstai.core.SahandSAT_Extended import SahandSATExtended
from sstai.core.SahandSAT_PySAT import SahandSATPySAT
from sstai.core.SahandKnapsack import SahandKnapsack


def test_wrappers_solve():
    clauses = [[1], [-1, 2]]
    weights = {1: 1.0, 2: 0.5}
    sol1 = SahandSAT(clauses=clauses, weights=weights).solve()
    try:
        sol2 = SahandSATPySAT(clauses=clauses, weights=weights).solve()
        assert sol1["min_weight"] == sol2["min_weight"]
    except ImportError:
        pass
    ext = SahandSATExtended()
    ext.load_and_solve({"clauses": clauses, "weights": weights})
    assert ext.solution is not None
    k = SahandKnapsack({"clauses": clauses, "weights": weights})
    assert "total_weight" in k.analyze_and_optimize()
