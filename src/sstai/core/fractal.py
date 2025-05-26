"""Fractal utilities."""

from typing import Iterable, List

try:  # Optional dependency
    import numpy as np
except Exception:  # pragma: no cover - missing optional dependency
    np = None


def compute_fractal(values: Iterable[float], iterations: int = 10) -> List[float]:
    """Simple Mandelbrot-like iteration for demo purposes."""
    result: List[float] = []
    for val in values:
        z = 0j
        c = complex(val, val)
        for _ in range(iterations):
            z = z * z + c
        result.append(z.real)
    return result


class FractalLattice:
    """Simple 3‑D lattice with a toy fractal update rule."""

    def __init__(self, layers: tuple[int, int, int] = (6, 13, 5), seed: int | None = None):
        if np is None:
            raise ImportError("numpy is required for FractalLattice")
        self.layers = layers
        self.rng = np.random.default_rng(seed)
        self.grid = self._init_grid()

    def _init_grid(self) -> 'np.ndarray':
        return np.zeros(self.layers, dtype=float)

    def iterate(self, steps: int = 1) -> None:
        for _ in range(steps):
            padded = np.pad(self.grid, 1)
            new = np.zeros_like(self.grid)
            it = np.nditer(self.grid, flags=["multi_index"])
            for _ in it:
                idx = tuple(i + 1 for i in it.multi_index)
                neighborhood = padded[
                    idx[0] - 1 : idx[0] + 2,
                    idx[1] - 1 : idx[1] + 2,
                    idx[2] - 1 : idx[2] + 2,
                ]
                new[it.multi_index] = neighborhood.mean()
            self.grid = new

    def as_vector(self) -> 'np.ndarray':
        return self.grid.flatten()

    def __repr__(self) -> str:  # pragma: no cover - simple representation
        return f"FractalLattice(layers={self.layers})"
