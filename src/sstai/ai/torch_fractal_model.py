"""PyTorch implementation of the fractal regression model."""

from __future__ import annotations

from typing import Iterable, List

try:
    import torch
    from torch import nn
except Exception as e:  # pragma: no cover - optional dependency
    torch = None
    nn = None

from sstai.core.fractal import _code_to_value, compute_fractal
from sstai.core.lemmas import load_lemmas


class TorchFractalModel:  # pragma: no cover - simple wrapper
    def __init__(self) -> None:
        if torch is None:
            raise ImportError("PyTorch is required for TorchFractalModel")
        self.linear = nn.Linear(1, 1)

    def predict(self, x: Iterable[float]) -> List[float]:
        if torch is None:
            raise ImportError("PyTorch is required for TorchFractalModel")
        with torch.no_grad():
            t = torch.tensor([[v] for v in x], dtype=torch.float32)
            return self.linear(t).squeeze(1).tolist()


def _load_dataset() -> tuple[list[float], list[float]]:
    lemmas = load_lemmas()
    codes = [lemma["code"] for lemma in lemmas]
    xs = [_code_to_value(c) for c in codes]
    ys = compute_fractal(xs)
    return xs, ys


def train_torch_fractal_model(epochs: int = 200, lr: float = 0.1) -> TorchFractalModel:
    if torch is None:
        raise ImportError("PyTorch is required for training")
    x, y = _load_dataset()
    model = TorchFractalModel()
    optim = torch.optim.SGD(model.linear.parameters(), lr=lr)
    loss_fn = nn.MSELoss()
    t_x = torch.tensor([[v] for v in x], dtype=torch.float32)
    t_y = torch.tensor([[v] for v in y], dtype=torch.float32)
    for _ in range(epochs):
        optim.zero_grad()
        pred = model.linear(t_x)
        loss = loss_fn(pred, t_y)
        loss.backward()
        optim.step()
    return model


def predict_torch_fractal(
    model: TorchFractalModel, codes: Iterable[str]
) -> List[float]:
    if torch is None:
        raise ImportError("PyTorch is required for prediction")
    x = [_code_to_value(c) for c in codes]
    return model.predict(x)
