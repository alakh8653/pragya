"""Messaging endpoints."""

from typing import List
from uuid import uuid4

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/messages", tags=["messaging"])


class Message(BaseModel):
    id: str
    sender_id: str
    receiver_id: str
    body: str


messages_db: List[Message] = []


@router.post("/", response_model=Message, status_code=201)
def send_message(message: Message) -> Message:
    message.id = str(uuid4())
    messages_db.append(message)
    return message


@router.get("/inbox/{user_id}", response_model=List[Message])
def inbox(user_id: str) -> List[Message]:
    return [m for m in messages_db if m.receiver_id == user_id]

