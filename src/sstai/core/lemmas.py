"""Utilities for loading Sahand Fractal Lemmas."""
from __future__ import annotations

from typing import List, Dict

from ..database import load_lemmas_from_db


def load_lemmas() -> List[Dict[str, str]]:
    """Load the 150 Sahand Fractal Lemmas from the database."""
    return load_lemmas_from_db()

