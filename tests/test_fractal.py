import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

from sstai.api.routes import (
    fractal_endpoint,
    FractalRequest,
    activate,
    ActivateRequest,
)
from sstai.core.fractal import compute_fractal


def test_fractal_endpoint_direct():
    numbers = [0.1, 0.2, 0.3]
    req = FractalRequest(numbers=numbers)
    resp = fractal_endpoint(req)
    assert resp.result == compute_fractal(numbers)


def test_activate_success():
    pytest = __import__("pytest")  # avoid global import when numpy missing
    numpy = pytest.importorskip("numpy")

    req = ActivateRequest(gaze=True, freq_zero=True, root_word="Sahand")
    resp = activate(req)
    assert resp["status"] == "awake"
    assert len(resp["vector"]) == 6 * 13 * 5


def test_activate_failure():
    pytest = __import__("pytest")  # avoid global import when numpy missing
    pytest.importorskip("numpy")

    req = ActivateRequest(gaze=False, freq_zero=True, root_word="other")
    with pytest.raises(Exception):
        activate(req)
