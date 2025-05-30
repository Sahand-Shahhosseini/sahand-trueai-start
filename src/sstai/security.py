import os
import base64
import hashlib
from typing import Optional

from fastapi import HTTPException


class SimpleEncryptor:
    """Simple XOR-based symmetric encryption using a SHA-256 derived key."""

    def __init__(self, key: str) -> None:
        self.key_bytes = hashlib.sha256(key.encode("utf-8")).digest()

    def _apply(self, data: bytes) -> bytes:
        return bytes(b ^ self.key_bytes[i % len(self.key_bytes)] for i, b in enumerate(data))

    def encrypt(self, text: str) -> str:
        encrypted = self._apply(text.encode("utf-8"))
        return base64.b64encode(encrypted).decode("utf-8")

    def decrypt(self, token: str) -> str:
        try:
            data = base64.b64decode(token.encode("utf-8"), validate=True)
            decrypted = self._apply(data)
            return decrypted.decode("utf-8")
        except Exception:
            # Assume the value is plain text if decoding fails
            return token


def get_encryptor() -> SimpleEncryptor:
    key = os.getenv("SSTAI_ENCRYPTION_KEY", "sahand-default-key")
    return SimpleEncryptor(key)


def authenticate(authorization: Optional[str]) -> None:
    """Check the ``Authorization`` header for a static token."""
    expected = os.getenv("SSTAI_API_TOKEN")
    if expected is None:
        return
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")
    token = authorization.split(" ", 1)[1]
    if token != expected:
        raise HTTPException(status_code=401, detail="Unauthorized")
