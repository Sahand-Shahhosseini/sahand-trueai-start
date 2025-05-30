from typing import Iterable, List

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


def _code_to_value(code: str) -> float:
    """Convert a lemma code like ``"SFL_001"`` to a normalized float."""
    digits = "".join(ch for ch in code if ch.isdigit())
    if not digits:
        raise ValueError(f"Invalid lemma code: {code}")
    return int(digits) / 150.0


def compute_fractal_from_codes(codes: Iterable[str], iterations: int = 10) -> List[float]:
    """Compute fractal results directly from lemma codes."""
    values = [_code_to_value(c) for c in codes]
    return compute_fractal(values, iterations)
