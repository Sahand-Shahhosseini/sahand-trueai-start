"""Demonstrate a simple reflective consciousness process."""
from __future__ import annotations

from typing import Iterable, List, Any


def reflective_process(inputs: Iterable[Any]) -> List[List[Any]]:
    """Return successive states for the given inputs.

    The special token ``"REFLECT"`` causes the system to append the
    previous state as an element, implementing self-reflection.
    """
    states: List[List[Any]] = []
    state: List[Any] = []

    for item in inputs:
        if item == "REFLECT" and states:
            state = state + [states[-1]]
        else:
            state = state + [item]
        states.append(list(state))
    return states


if __name__ == "__main__":
    sequence = ["light", "light", "light", "REFLECT"]
    all_states = reflective_process(sequence)
    for i, s in enumerate(all_states, start=1):
        print(f"Psi_{i} = {s}")
