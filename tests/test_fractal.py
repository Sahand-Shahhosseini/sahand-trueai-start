import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

from sstai.api.routes import (
    fractal_endpoint,
    FractalRequest,
    lemma_fractal_endpoint,
    LemmaFractalRequest,
)
from sstai.core.fractal import compute_fractal, compute_fractal_from_codes


def test_fractal_endpoint_direct():
    numbers = [0.1, 0.2, 0.3]
    req = FractalRequest(numbers=numbers)
    resp = fractal_endpoint(req)
    assert resp.result == compute_fractal(numbers)


def test_compute_fractal_normalized():
    numbers = [1.0, 2.0, 3.0]
    result = compute_fractal(numbers)
    assert abs(sum(result) - 1.0) < 1e-6


def test_lemma_fractal_endpoint():
    codes = ["SFL_001", "SFL_002", "SFL_003"]
    req = LemmaFractalRequest(codes=codes)
    resp = lemma_fractal_endpoint(req)
    assert resp.result == compute_fractal_from_codes(codes)


def test_compute_fractal_from_codes():
    codes = ["SFL_001", "SFL_005"]
    values = compute_fractal_from_codes(codes)
    assert isinstance(values, list) and len(values) == len(codes)
