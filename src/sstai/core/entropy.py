from __future__ import annotations
import math
import random
from typing import Sequence, List


def entropy(state: Sequence[complex | float]) -> float:
    """Shannon entropy of the probability distribution derived from a state."""
    prob = [abs(x) ** 2 for x in state]
    total = sum(prob)
    if total == 0:
        return 0.0
    prob = [p / total for p in prob]
    return -sum(p * math.log(p) for p in prob if p > 0)


def collapse(state: Sequence[complex | float], rng: random.Random | None = None) -> List[complex]:
    """Projective measurement in the computational basis."""
    prob = [abs(x) ** 2 for x in state]
    total = sum(prob)
    if total == 0:
        raise ValueError("state has zero norm")
    prob = [p / total for p in prob]
    if rng is None:
        rng = random.Random()
    idx = rng.choices(range(len(state)), weights=prob, k=1)[0]
    collapsed = [0j for _ in state]
    collapsed[idx] = 1 + 0j
    return collapsed
