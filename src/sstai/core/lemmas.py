"""Utilities for loading Sahand Fractal Lemmas."""
from __future__ import annotations

import json
from importlib import resources
from typing import List, Dict


def load_lemmas() -> List[Dict[str, str]]:
    """Load the 150 Sahand Fractal Lemmas from packaged JSON data."""
    with resources.open_text("sstai.data", "lemmas.json", encoding="utf-8") as f:
        return json.load(f)

