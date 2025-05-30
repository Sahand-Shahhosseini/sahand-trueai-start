import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

from sstai.ai.rewrite import (
    add_interaction,
    load_interactions,
    clear_interactions,
    train_fractal_model_with_interactions,
)
from sstai.ai import predict_fractal
from sstai.core.fractal import compute_fractal_from_codes


def test_learning_rewrite_workflow():
    clear_interactions()
    codes = ['SFL_010', 'SFL_011']
    target = compute_fractal_from_codes(codes)
    add_interaction(codes, target)
    interactions = load_interactions()
    assert interactions[-1].codes == codes
    model = train_fractal_model_with_interactions(epochs=10, lr=0.1)
    preds = predict_fractal(model, codes)
    assert len(preds) == len(codes)
