import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sstai.persona import load_persona_text


def test_load_persona_text():
    text = load_persona_text()
    assert "STAI" in text
