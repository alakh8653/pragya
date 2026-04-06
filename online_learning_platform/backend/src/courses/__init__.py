"""Course related endpoints."""

from typing import List, Optional
from uuid import uuid4

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/courses", tags=["courses"])


class Course(BaseModel):
    id: str
    title: str
    description: Optional[str] = None


class CourseCreate(BaseModel):
    title: str
    description: Optional[str] = None


courses_db: List[Course] = []


@router.post("/", response_model=Course, status_code=201)
async def create_course(course: CourseCreate) -> Course:
    """Add a course to the in-memory database."""
    course_obj = Course(id=str(uuid4()), **course.dict())
    courses_db.append(course_obj)
    return course_obj


@router.get("/", response_model=List[Course])
async def list_courses() -> List[Course]:
    return courses_db


@router.get("/{course_id}", response_model=Course)
async def get_course(course_id: str) -> Course:
    for course in courses_db:
        if course.id == course_id:
            return course
    raise HTTPException(status_code=404, detail="Course not found")


@router.put("/{course_id}", response_model=Course)
async def update_course(course_id: str, data: CourseCreate) -> Course:
    for idx, course in enumerate(courses_db):
        if course.id == course_id:
            updated = course.copy(update=data.dict())
            courses_db[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Course not found")


@router.delete("/{course_id}", status_code=204)
async def delete_course(course_id: str) -> None:
    for idx, course in enumerate(courses_db):
        if course.id == course_id:
            del courses_db[idx]
            return
    raise HTTPException(status_code=404, detail="Course not found")

