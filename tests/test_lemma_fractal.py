import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

from sstai.api.routes import lemma_fractal_endpoint, LemmaFractalRequest
from sstai.core.fractal import compute_fractal_from_codes


def test_lemma_fractal_endpoint():
    codes = ['SFL_001', 'SFL_002', 'SFL_003']
    req = LemmaFractalRequest(codes=codes)
    resp = lemma_fractal_endpoint(req)
    assert resp.result == compute_fractal_from_codes(codes)
