import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import math
import random
from sstai.core.entropy import entropy, collapse


def test_entropy_ln2():
    s = [1/math.sqrt(2), 1/math.sqrt(2)]
    assert abs(entropy(s) - math.log(2)) < 1e-6


def test_collapse_normalizes():
    rng = random.Random(0)
    state = [1j, 0]
    c = collapse(state, rng)
    norm = math.sqrt(sum(abs(x)**2 for x in c))
    assert abs(norm - 1.0) < 1e-6
    assert c.count(1+0j) == 1
