from typing import Iterable, List

from .field import normalize


def compute_fractal(values: Iterable[float], iterations: int = 10) -> List[float]:
    """Simple Mandelbrot-like iteration with normalization."""
    result: List[float] = []
    for val in values:
        z = 0j
        c = complex(val, val)
        for _ in range(iterations):
            z = z * z + c
            if abs(z) > 2:
                break
        result.append(z.real)
    return normalize(result)
