"""Assignment endpoints."""

from typing import List
from uuid import uuid4

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/assignments", tags=["assignments"])


class Assignment(BaseModel):
    id: str
    course_id: str
    title: str


class AssignmentCreate(BaseModel):
    course_id: str
    title: str


assignments_db: List[Assignment] = []


@router.post("/", response_model=Assignment, status_code=201)
def create_assignment(payload: AssignmentCreate) -> Assignment:
    assignment = Assignment(id=str(uuid4()), **payload.dict())
    assignments_db.append(assignment)
    return assignment


@router.get("/", response_model=List[Assignment])
def list_assignments() -> List[Assignment]:
    return assignments_db

