from typing import Iterable, List


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
