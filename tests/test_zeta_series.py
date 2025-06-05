import pytest

pytest.importorskip("mpmath")

import mpmath as mp

from examples.zeta_series import partial_zeta, tail_bound


def test_partial_zeta_close():
    s = 2
    approx = partial_zeta(s, 1000)
    assert abs(approx - mp.zeta(s)) < mp.mpf("1e-6")


def test_tail_bound():
    s = 2
    N = 10
    bound = tail_bound(s, N)
    remainder = mp.zeta(s) - partial_zeta(s, N)
    assert abs(remainder) <= bound
