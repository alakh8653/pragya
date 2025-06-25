"""Basic analytics endpoints."""

from fastapi import APIRouter

from backend.src.courses import courses_db
from backend.src.users import users_db

router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get("/summary")
def summary():
    """Return simple usage statistics."""
    return {"users": len(users_db), "courses": len(courses_db)}

