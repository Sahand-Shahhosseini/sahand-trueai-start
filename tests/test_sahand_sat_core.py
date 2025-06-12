from sat_solver.SahandSAT_Core import SahandSATCore


def test_core_bruteforce():
    clauses = [[1, 2], [-1, 2]]
    weights = {1: 1.0, 2: 0.5}
    solver = SahandSATCore(clauses=clauses, weights=weights)
    result = solver.solve_bruteforce()
    assert result["min_weight"] == 0.5
    assert result["assignment"][2] is True
    assert result["assignment"][1] is False
