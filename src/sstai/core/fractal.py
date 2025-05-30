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


def _code_to_value(code: str) -> float:
    """Map a lemma code like ``SFL_001`` to a numeric value."""
    try:
        number = int(code.split("_")[1])
    except (IndexError, ValueError) as exc:
        raise ValueError(f"invalid lemma code: {code}") from exc
    return number / 150.0


def compute_fractal_from_codes(codes: Iterable[str], iterations: int = 10) -> List[float]:
    """Compute a fractal result using lemma codes as input."""
    values = [_code_to_value(c) for c in codes]
    return compute_fractal(values, iterations=iterations)

