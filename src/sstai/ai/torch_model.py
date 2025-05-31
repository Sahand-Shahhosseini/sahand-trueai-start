from __future__ import annotations

from typing import Iterable, List

try:  # pragma: no cover - optional dependency
    import torch
    from torch import nn
    from torch.utils.data import DataLoader, TensorDataset
except Exception:  # pragma: no cover - torch may be missing
    torch = None  # type: ignore
    nn = None  # type: ignore
    DataLoader = TensorDataset = None  # type: ignore

from sstai.core.fractal import compute_fractal, _code_to_value
from sstai.core.lemmas import load_lemmas


if nn is not None:

    class TorchFractalNet(nn.Module):
        """Minimal single-layer network for fractal prediction."""

        def __init__(self) -> None:
            super().__init__()
            self.linear = nn.Linear(1, 1)

        def forward(self, x: torch.Tensor) -> torch.Tensor:  # pragma: no cover - thin
            return self.linear(x)

else:  # pragma: no cover - torch missing

    class TorchFractalNet:  # type: ignore
        pass


def _load_dataset() -> tuple[torch.Tensor, torch.Tensor]:
    if torch is None:
        raise ImportError("PyTorch is required for TorchFractalNet")
    lemmas = load_lemmas()
    codes = [lemma["code"] for lemma in lemmas]
    x = torch.tensor([_code_to_value(c) for c in codes], dtype=torch.float32).unsqueeze(
        1
    )
    y = torch.tensor(
        compute_fractal(x.squeeze().tolist()), dtype=torch.float32
    ).unsqueeze(1)
    return x, y


def train_torch_fractal_model(epochs: int = 50, lr: float = 0.1) -> TorchFractalNet:
    """Return a trained :class:`TorchFractalNet`."""
    if torch is None:
        raise ImportError("PyTorch is required for TorchFractalNet")
    x, y = _load_dataset()
    dataset = TensorDataset(x, y)
    loader = DataLoader(dataset, batch_size=16, shuffle=True)
    model = TorchFractalNet()
    opt = torch.optim.SGD(model.parameters(), lr=lr)
    for _ in range(epochs):
        for bx, by in loader:
            opt.zero_grad()
            pred = model(bx)
            loss = nn.functional.mse_loss(pred, by)
            loss.backward()
            opt.step()
    return model


def predict_torch_fractal(model: TorchFractalNet, codes: Iterable[str]) -> List[float]:
    """Predict fractal values for lemma codes using ``model``."""
    if torch is None:
        raise ImportError("PyTorch is required for TorchFractalNet")
    x = torch.tensor([_code_to_value(c) for c in codes], dtype=torch.float32).unsqueeze(
        1
    )
    with torch.no_grad():
        preds = model(x).squeeze().tolist()
    if isinstance(preds, float):
        return [float(preds)]
    return [float(p) for p in preds]
