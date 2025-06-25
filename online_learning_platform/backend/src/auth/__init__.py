"""Simple authentication endpoints."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.src.users import users_db

router = APIRouter(prefix="/auth", tags=["auth"])


class LoginRequest(BaseModel):
    email: str
    password: str


@router.post("/login")
def login(credentials: LoginRequest):
    """Very basic login that validates by email only."""
    for user in users_db:
        if user.email == credentials.email:
            return {"token": f"fake-token-for-{user.id}"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

