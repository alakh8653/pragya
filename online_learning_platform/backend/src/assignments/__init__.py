"""Assignment endpoints."""

from typing import List
from uuid import uuid4

from fastapi import APIRouter, HTTPException
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
async def create_assignment(payload: AssignmentCreate) -> Assignment:
    assignment = Assignment(id=str(uuid4()), **payload.dict())
    assignments_db.append(assignment)
    return assignment


@router.get("/", response_model=List[Assignment])
async def list_assignments() -> List[Assignment]:
    return assignments_db


@router.get("/{assignment_id}", response_model=Assignment)
async def get_assignment(assignment_id: str) -> Assignment:
    for assn in assignments_db:
        if assn.id == assignment_id:
            return assn
    raise HTTPException(status_code=404, detail="Assignment not found")


@router.delete("/{assignment_id}", status_code=204)
async def delete_assignment(assignment_id: str) -> None:
    for idx, assn in enumerate(assignments_db):
        if assn.id == assignment_id:
            del assignments_db[idx]
            return
    raise HTTPException(status_code=404, detail="Assignment not found")

