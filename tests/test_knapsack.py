import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

import math
from sstai.core import sahand_knapsack


def test_sahand_knapsack_selects_best():
    psi0 = [1.0, 0.0]
    psi1 = [0.0, 1.0]
    psip = [(psi0[0] + psi1[0]) / math.sqrt(2), (psi0[1] + psi1[1]) / math.sqrt(2)]
    G = [[1.0, 0.0], [0.0, 0.9]]
    selected = sahand_knapsack([psi0, psi1, psip], psi0, G)
    assert all(abs(a - b) < 1e-9 for a, b in zip(selected, psi0))
