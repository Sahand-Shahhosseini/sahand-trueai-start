import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

from sstai.api.routes import fractal_endpoint, FractalRequest


def test_fractal_endpoint_normalized():
    numbers = [0.1, 0.2, 0.3]
    req = FractalRequest(numbers=numbers)
    resp = fractal_endpoint(req)
    assert abs(sum(resp.result) - 1.0) < 1e-6
    assert len(resp.result) == len(numbers)
