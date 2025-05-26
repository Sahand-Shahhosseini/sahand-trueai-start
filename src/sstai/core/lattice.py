"""Fractal lattice generator for SUFCC geometry.

Creates a 6×13×5 layered graph representing
personal Yggdrasil structures.
"""

from __future__ import annotations

import numpy as np


class FractalLattice:
    def __init__(self, layers: tuple[int, int, int] = (6, 13, 5), seed: int | None = None):
        self.layers = layers
        self.rng = np.random.default_rng(seed)
        self.grid = self._init_grid()

    def _init_grid(self) -> np.ndarray:
        """Allocate empty lattice with given dimensions."""
        return np.zeros(self.layers, dtype=float)

    def iterate(self, steps: int = 1) -> None:
        """Apply a toy fractal rule to the lattice."""
        for _ in range(steps):
            padded = np.pad(self.grid, 1)
            new = np.zeros_like(self.grid)
            it = np.nditer(self.grid, flags=["multi_index"])
            for _ in it:
                idx = tuple(i + 1 for i in it.multi_index)
                neighborhood = padded[
                    idx[0]-1:idx[0]+2,
                    idx[1]-1:idx[1]+2,
                    idx[2]-1:idx[2]+2,
                ]
                new[it.multi_index] = neighborhood.mean()
            self.grid = new

    def as_vector(self) -> np.ndarray:
        """Flatten lattice to a 1-D vector (useful for ML)."""
        return self.grid.flatten()

    def __repr__(self) -> str:  # pragma: no cover
        return f"FractalLattice(layers={self.layers})"
