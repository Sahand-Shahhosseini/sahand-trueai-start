from sat_solver.SahandKnapsack import SahandKnapsack


def test_knapsack_optimize():
    problem = {"clauses": [[1, 2], [-1, 2]], "weights": {"1": 1.0, "2": 0.5}}
    knapsack = SahandKnapsack(problem)
    result = knapsack.optimize()
    assert result["min_weight"] == 0.5
    assert result["assignment"][2] is True
    assert result["assignment"][1] is False
