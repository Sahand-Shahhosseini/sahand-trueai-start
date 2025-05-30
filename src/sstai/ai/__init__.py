"""Simple machine learning utilities."""

from .fractal_model import FractalModel, train_fractal_model, predict_fractal
from .rewrite import (
    add_interaction,
    load_interactions,
    clear_interactions,
    train_fractal_model_with_interactions,
)

__all__ = [
    'FractalModel',
    'train_fractal_model',
    'predict_fractal',
    'add_interaction',
    'load_interactions',
    'clear_interactions',
    'train_fractal_model_with_interactions',
]
