"""Assessment endpoints."""

from typing import List
from uuid import uuid4

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/assessments", tags=["assessments"])


class Assessment(BaseModel):
    id: str
    title: str


class AssessmentCreate(BaseModel):
    title: str


class AssessmentUpdate(BaseModel):
    title: str


assessments_db: List[Assessment] = []


@router.post("/", response_model=Assessment, status_code=201)
async def create_assessment(data: AssessmentCreate) -> Assessment:
    assessment = Assessment(id=str(uuid4()), **data.dict())
    assessments_db.append(assessment)
    return assessment


@router.get("/", response_model=List[Assessment])
async def list_assessments() -> List[Assessment]:
    return assessments_db


@router.get("/{assessment_id}", response_model=Assessment)
async def get_assessment(assessment_id: str) -> Assessment:
    for assessment in assessments_db:
        if assessment.id == assessment_id:
            return assessment
    raise HTTPException(status_code=404, detail="Assessment not found")


@router.put("/{assessment_id}", response_model=Assessment)
async def update_assessment(assessment_id: str, data: AssessmentUpdate) -> Assessment:
    """Update assessment details."""
    for idx, assessment in enumerate(assessments_db):
        if assessment.id == assessment_id:
            updated = assessment.copy(update=data.dict(exclude_unset=True))
            assessments_db[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Assessment not found")


@router.delete("/{assessment_id}", status_code=204)
async def delete_assessment(assessment_id: str) -> None:
    for idx, assessment in enumerate(assessments_db):
        if assessment.id == assessment_id:
            del assessments_db[idx]
            return
    raise HTTPException(status_code=404, detail="Assessment not found")

