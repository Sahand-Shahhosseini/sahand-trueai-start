import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

from sstai.core import theta_diss


def test_theta_diss_example():
    value = theta_diss(60)
    assert abs(value - 2393.1188) < 1e-3
