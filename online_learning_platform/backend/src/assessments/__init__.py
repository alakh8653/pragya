"""Assessment endpoints."""

from typing import List
from uuid import uuid4

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/assessments", tags=["assessments"])


class Assessment(BaseModel):
    id: str
    title: str


class AssessmentCreate(BaseModel):
    title: str


assessments_db: List[Assessment] = []


@router.post("/", response_model=Assessment, status_code=201)
def create_assessment(data: AssessmentCreate) -> Assessment:
    assessment = Assessment(id=str(uuid4()), **data.dict())
    assessments_db.append(assessment)
    return assessment


@router.get("/", response_model=List[Assessment])
def list_assessments() -> List[Assessment]:
    return assessments_db

