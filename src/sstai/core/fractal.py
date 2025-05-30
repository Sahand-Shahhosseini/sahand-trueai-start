from typing import Iterable, List
import re

from .lemmas import load_lemmas

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


_LEMMA_MAP = None


def _code_to_value(code: str) -> float:
    m = re.search(r"(\d+)$", code)
    if not m:
        raise ValueError(f"invalid code: {code}")
    return int(m.group(1)) / 100.0


def compute_fractal_from_codes(codes: Iterable[str], iterations: int = 10) -> List[float]:
    """Compute fractal values from lemma codes."""
    values = [_code_to_value(c) for c in codes]
    return compute_fractal(values, iterations=iterations)
