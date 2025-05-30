import pytest

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

from sstai import security
from sstai.security import verify_api_key, API_KEY
from fastapi import HTTPException


def test_verify_api_key_valid():
    assert verify_api_key(f"Bearer {API_KEY}") is None


def test_verify_api_key_invalid():
    with pytest.raises(HTTPException):
        verify_api_key("invalid")
