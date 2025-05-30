"""Utilities for loading Sahand Fractal Lemmas."""
from __future__ import annotations

import json
from importlib import resources
from typing import List, Dict

from sstai.security import xor_decrypt


def load_lemmas(key: bytes = b"mysecretkey") -> List[Dict[str, str]]:
    """Load and decrypt the 150 Sahand Fractal Lemmas."""
    with resources.open_text("sstai.data", "lemmas.enc", encoding="utf-8") as f:
        encoded = f.read()
    data = xor_decrypt(encoded, key)
    return json.loads(data.decode("utf-8"))

