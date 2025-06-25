"""Notification endpoints."""

from typing import List
from uuid import uuid4

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/notifications", tags=["notifications"])


class Notification(BaseModel):
    id: str
    user_id: str
    text: str


notifications_db: List[Notification] = []


@router.post("/", response_model=Notification, status_code=201)
def create_notification(notification: Notification) -> Notification:
    notification.id = str(uuid4())
    notifications_db.append(notification)
    return notification


@router.get("/{user_id}", response_model=List[Notification])
def get_notifications(user_id: str) -> List[Notification]:
    return [n for n in notifications_db if n.user_id == user_id]

