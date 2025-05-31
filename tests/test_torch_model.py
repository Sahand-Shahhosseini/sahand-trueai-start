import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pytest

from sstai.ai import train_torch_fractal_model, predict_torch_fractal


def test_torch_fractal_model():
    pytest.importorskip("torch")
    model = train_torch_fractal_model(epochs=10, lr=0.1)
    preds = predict_torch_fractal(model, ["SFL_001"])
    assert len(preds) == 1
    assert isinstance(preds[0], float)
