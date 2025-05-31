import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sstai.core.sahand_knapsack import SahandKnapsack


def test_sahand_knapsack_integration():
    problem = {
        "variables": ["x1", "x2"],
        "weights": {"x1": 1, "x2": 2},
        "clauses": [[1], [2]],
    }
    knapsack = SahandKnapsack(problem)
    result = knapsack.analyze_and_optimize()
    assert result["selected_variables"] == ["x1"]
    assert result["total_weight"] == 1
    assert "time" in result
