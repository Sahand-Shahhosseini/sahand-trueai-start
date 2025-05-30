from fastapi import Header, HTTPException
from typing import Optional

API_KEY = "SECRET_KEY"


def verify_api_key(authorization: Optional[str] = Header(None)) -> None:
    expected = f"Bearer {API_KEY}"
    if authorization != expected:
        raise HTTPException(status_code=401, detail="Unauthorized")


def authenticate(authorization: Optional[str]) -> None:
    verify_api_key(authorization)
