"""User management endpoints."""

from typing import List
from uuid import uuid4

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter(prefix="/users", tags=["users"])


class User(BaseModel):
    id: str
    name: str
    email: str


class UserCreate(BaseModel):
    name: str
    email: str


users_db: List[User] = []


@router.post("/", response_model=User, status_code=201)
def create_user(user: UserCreate) -> User:
    """Create a new user and store it in memory."""
    user_obj = User(id=str(uuid4()), **user.dict())
    users_db.append(user_obj)
    return user_obj


@router.get("/", response_model=List[User])
def list_users() -> List[User]:
    """Return all registered users."""
    return users_db


@router.get("/{user_id}", response_model=User)
def get_user(user_id: str) -> User:
    """Retrieve a single user by identifier."""
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

