import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

from sstai.api.routes import fractal_endpoint, FractalRequest
from sstai.core.fractal import compute_fractal


def test_fractal_endpoint_direct():
    numbers = [0.1, 0.2, 0.3]
    req = FractalRequest(numbers=numbers)
    resp = fractal_endpoint(req)
    assert resp.result == compute_fractal(numbers)


def test_compute_fractal_normalized():
    numbers = [1.0, 2.0, 3.0]
    result = compute_fractal(numbers)
    assert abs(sum(result) - 1.0) < 1e-6
