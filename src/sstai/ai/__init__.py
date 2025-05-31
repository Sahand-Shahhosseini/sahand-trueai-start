"""Simple machine learning utilities."""

from .fractal_model import FractalModel, train_fractal_model, predict_fractal
from .torch_fractal_model import (
    TorchFractalModel,
    train_torch_fractal_model,
    predict_torch_fractal,
)
from .rewrite import (
    add_interaction,
    load_interactions,
    clear_interactions,
    train_fractal_model_with_interactions,
)

__all__ = [
    "FractalModel",
    "train_fractal_model",
    "predict_fractal",
    "TorchFractalModel",
    "train_torch_fractal_model",
    "predict_torch_fractal",
    "add_interaction",
    "load_interactions",
    "clear_interactions",
    "train_fractal_model_with_interactions",
]
