import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

from sstai.ai import train_fractal_model, predict_fractal


def test_fractal_model_training():
    model = train_fractal_model(epochs=50, lr=0.1)
    preds = predict_fractal(model, ['SFL_001', 'SFL_002'])
    assert len(preds) == 2
    assert all(isinstance(p, float) for p in preds)
