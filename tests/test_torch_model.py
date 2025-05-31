import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

pytest.importorskip("torch")

from sstai.ai import train_torch_fractal_model, predict_torch_fractal


def test_torch_model_training():
    model = train_torch_fractal_model(epochs=10, lr=0.1)
    preds = predict_torch_fractal(model, ["SFL_001"])
    assert len(preds) == 1
    assert isinstance(preds[0], float)
