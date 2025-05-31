import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sstai.persona import load_persona_text

if __name__ == "__main__":
    print("\U0001f7e2 Core online")
    print(load_persona_text())
