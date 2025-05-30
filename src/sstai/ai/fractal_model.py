"""Pure Python regression model for fractal outputs."""
from __future__ import annotations

from typing import Iterable, Tuple, List
import random

from sstai.core.fractal import compute_fractal, _code_to_value
from sstai.core.lemmas import load_lemmas


class FractalModel:
    """Linear model ``y = w * x + b`` trained via gradient descent."""

    def __init__(self) -> None:
        self.w = random.random()
        self.b = random.random()

    def predict(self, x: Iterable[float]) -> List[float]:  # pragma: no cover - trivial
        return [self.w * v + self.b for v in x]


def _load_dataset() -> Tuple[List[float], List[float]]:
    lemmas = load_lemmas()
    codes = [lemma["code"] for lemma in lemmas]
    xs = [_code_to_value(c) for c in codes]
    ys = compute_fractal(xs)
    return xs, ys


def train_fractal_model(epochs: int = 200, lr: float = 0.5) -> FractalModel:
    """Return a trained :class:`FractalModel`."""
    x, y = _load_dataset()
    model = FractalModel()
    n = len(x)
    for _ in range(epochs):
        preds = model.predict(x)
        grad_w = sum((p - t) * xv for p, t, xv in zip(preds, y, x)) * 2 / n
        grad_b = sum(p - t for p, t in zip(preds, y)) * 2 / n
        model.w -= lr * grad_w
        model.b -= lr * grad_b
    return model


def predict_fractal(model: FractalModel, codes: Iterable[str]) -> List[float]:
    """Predict fractal values for lemma codes using ``model``."""
    x = [_code_to_value(c) for c in codes]
    return model.predict(x)
