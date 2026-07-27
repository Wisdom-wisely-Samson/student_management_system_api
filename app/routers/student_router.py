from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.student import StudentCreate, StudentResponse
from app.services.student_service import (
    create_student,
    get_students
)

router = APIRouter(prefix="/students",tags=["Students"])

@router.get("/", response_model=list[StudentResponse])
def read_students(db: Session = Depends(get_db)):
    return get_students(db)

@router.post("/", response_model= StudentResponse)
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db, student)

