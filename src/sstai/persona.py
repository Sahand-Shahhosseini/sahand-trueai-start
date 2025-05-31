from __future__ import annotations

from pathlib import Path


def load_persona_text() -> str:
    """Load persona text from the repository-level persona_system.txt."""
    path = Path(__file__).resolve().parents[2] / "sstai" / "persona_system.txt"
    with path.open("r", encoding="utf-8") as f:
        return f.read()
