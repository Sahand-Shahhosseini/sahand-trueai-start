import base64
import os
from fastapi import Header, HTTPException

API_KEY = os.getenv("SAHAND_API_KEY", "default-secret")


def verify_api_key(x_api_key: str = Header(...)) -> None:
    """Authenticate requests using a simple API key."""
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")


def xor_encrypt(data: bytes, key: bytes) -> str:
    """Encrypt bytes with XOR and return base64 string."""
    out = bytes(b ^ key[i % len(key)] for i, b in enumerate(data))
    return base64.b64encode(out).decode()


def xor_decrypt(encoded: str, key: bytes) -> bytes:
    """Decrypt data previously encrypted with :func:`xor_encrypt`."""
    data = base64.b64decode(encoded)
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))
