import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sstai.persona import load_persona_text


def main():
    print("\U0001F7E2 Core online")
    print(load_persona_text())


if __name__ == "__main__":
    main()
