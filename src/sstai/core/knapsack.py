"""Sahand Knapsack selection utilities."""
from __future__ import annotations

from typing import Iterable, List, Sequence

import math


def entropy(psi: Sequence[complex]) -> float:
    """Compute a Shannon-like entropy of the amplitude magnitudes."""
    norm = sum(abs(x) ** 2 for x in psi)
    if norm == 0:
        return 0.0
    ent = 0.0
    for x in psi:
        p = abs(x) ** 2 / norm
        if p > 1e-12:
            ent -= p * math.log(p)
    return ent


def angle(psi1: Sequence[complex], psi2: Sequence[complex]) -> float:
    """Return the angle between two state vectors."""
    dot = sum(complex(a).conjugate() * complex(b) for a, b in zip(psi1, psi2))
    norm1 = math.sqrt(sum(abs(a) ** 2 for a in psi1))
    norm2 = math.sqrt(sum(abs(b) ** 2 for b in psi2))
    if norm1 == 0 or norm2 == 0:
        return math.pi / 2
    cos_theta = abs(dot) / (norm1 * norm2)
    cos_theta = max(0.0, min(1.0, cos_theta))
    return math.acos(cos_theta)


def resonance(psi: Sequence[complex], G: Sequence[Sequence[complex]]) -> float:
    """Resonance metric with the knowledge field tensor ``G``."""
    result = 0j
    for i, psi_i in enumerate(psi):
        acc = 0j
        row = G[i]
        for j, psi_j in enumerate(psi):
            acc += row[j] * psi_j
        result += complex(psi_i).conjugate() * acc
    return result.real


def cost(
    psi: Sequence[complex],
    L_father: Sequence[complex],
    G: Sequence[Sequence[complex]],
    lambda1: float = 1.0,
    lambda2: float = 1.0,
    lambda3: float = 2.0,
) -> float:
    """Compute the selection cost for a candidate state."""
    return (
        lambda1 * angle(psi, L_father) ** 2
        + lambda2 * entropy(psi)
        - lambda3 * resonance(psi, G)
    )


def sahand_knapsack(
    basis: Iterable[Sequence[complex]],
    L_father: Sequence[complex],
    G: Sequence[Sequence[complex]],
) -> List[complex]:
    """Select the lowest-cost candidate from ``basis``."""
    candidates: List[Sequence[complex]] = list(basis)
    if not candidates:
        raise ValueError("basis must contain at least one candidate")
    return list(min(candidates, key=lambda psi: cost(psi, L_father, G)))
