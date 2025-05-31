import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from examples.chat_cli import chat_loop


def test_chat_loop_callable():
    assert callable(chat_loop)
