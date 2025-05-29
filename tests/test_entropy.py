import sys
from pathlib import Path
import math

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

from sstai.core.entropy import entropy, collapse


def test_entropy_ln2():
    probs = [0.5, 0.5]
    assert abs(entropy(probs) - math.log(2)) < 1e-9


def test_collapse_basic():
    state = [1+0j, 0j]
    assert collapse(state) == [1.0, 0.0]
