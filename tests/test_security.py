import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

import pytest
from fastapi import HTTPException
from sstai.security import xor_encrypt, xor_decrypt, verify_api_key, API_KEY


def test_xor_roundtrip():
    data = b"secret data"
    key = b"key"
    enc = xor_encrypt(data, key)
    dec = xor_decrypt(enc, key)
    assert dec == data


def test_verify_api_key():
    verify_api_key(API_KEY)
    with pytest.raises(HTTPException):
        verify_api_key("wrong")
