from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable, List

from .fractal_model import (
    FractalModel,
    _load_dataset,
    _code_to_value,
)

# Path to persisted interactions json
INTERACTIONS_FILE = Path(__file__).resolve().parents[1] / "data" / "interactions.json"

@dataclass
class Interaction:
    codes: List[str]
    results: List[float]


def _load_interactions() -> List[Interaction]:
    if not INTERACTIONS_FILE.exists():
        return []
    with INTERACTIONS_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return [Interaction(**d) for d in data]


def _save_interactions(interactions: List[Interaction]) -> None:
    INTERACTIONS_FILE.parent.mkdir(exist_ok=True)
    with INTERACTIONS_FILE.open("w", encoding="utf-8") as f:
        json.dump([asdict(i) for i in interactions], f, ensure_ascii=False, indent=2)


def add_interaction(codes: Iterable[str], results: Iterable[float]) -> None:
    """Append a new user interaction to the persistent store."""
    interactions = _load_interactions()
    interactions.append(Interaction(list(codes), list(results)))
    _save_interactions(interactions)


def load_interactions() -> List[Interaction]:
    """Return all stored interactions."""
    return _load_interactions()


def clear_interactions() -> None:
    """Remove all stored interactions."""
    _save_interactions([])


def train_fractal_model_with_interactions(epochs: int = 200, lr: float = 0.5) -> FractalModel:
    """Train a :class:`FractalModel` using both built-in data and stored interactions."""
    x, y = _load_dataset()
    interactions = _load_interactions()
    for inter in interactions:
        x.extend([_code_to_value(c) for c in inter.codes])
        y.extend(inter.results)
    model = FractalModel()
    n = len(x)
    for _ in range(epochs):
        preds = model.predict(x)
        grad_w = sum((p - t) * xv for p, t, xv in zip(preds, y, x)) * 2 / n
        grad_b = sum(p - t for p, t in zip(preds, y)) * 2 / n
        model.w -= lr * grad_w
        model.b -= lr * grad_b
    return model
