import math
from typing import Iterable, List


def entropy(probs: Iterable[float]) -> float:
    total = 0.0
    for p in probs:
        if p > 0:
            total -= p * math.log(p)
    return total


def collapse(state: Iterable[complex]) -> List[float]:
    norm = sum(abs(a) ** 2 for a in state)
    if norm == 0:
        return [0 for _ in state]
    return [abs(a) ** 2 / norm for a in state]
