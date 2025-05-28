import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

from sstai.core import load_lemmas


def test_load_lemmas_count():
    lemmas = load_lemmas()
    assert len(lemmas) == 150


def test_first_lemma_code_title():
    lemmas = load_lemmas()
    assert lemmas[0]["code"] == "SFL_001"
    assert "نگاه" in lemmas[0]["title"]
