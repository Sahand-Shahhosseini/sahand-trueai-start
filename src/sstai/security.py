"""Simple authentication utilities."""

import os
from typing import Optional

from fastapi import HTTPException


def authenticate(authorization: Optional[str]) -> None:
    """Verify the ``Authorization`` header matches ``SSTAI_API_TOKEN``."""
    expected = os.getenv("SSTAI_API_TOKEN")
    if expected is None:
        return
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")
    token = authorization.split(" ", 1)[1]
    if token != expected:
        raise HTTPException(status_code=401, detail="Unauthorized")

