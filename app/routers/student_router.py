from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.database import get_db
from app.schemas.student import StudentCreate, StudentUpdate, StudentResponse
from app.services.student_service import (
    create_student,
    get_students,
    search_students,
    get_student_by_id,
    update_student,
    delete_student
)

router = APIRouter(prefix="/students",tags=["Students"])

@router.get("/", response_model=list[StudentResponse])
def read_students(skip: int = Query(default = 0, ge=1, description = "Number of students to skip"), limit: int = Query(default = 10, ge = 1, le = 100, description = "Maximum number of students to return"),db: Session = Depends(get_db)):
    return get_students(db, skip=skip, limit=limit)

@router.post("/", response_model= StudentResponse)
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db, student)
@router.get("/search", response_model=list[StudentResponse])
def search_student(name: str | None = Query(default = None, min_length=1), course: str | None = Query(default = None, min_length= 1), db: Session = Depends(get_db)):
    return search_students(db, name=name, course=course)

@router.get("/{student_id}", response_model=StudentResponse)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = get_student_by_id(db, student_id)

    if student is  None:
        raise HTTPException(status_code=404, detail="Student not found!")
    return student
@router.put("/{student_id}", response_model=StudentResponse)
def edit_student(student_id: int, student: StudentUpdate, db: Session = Depends(get_db)):
    updated_student = update_student(db, student_id, student)

    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found!")
    return updated_student
@router.delete("/{student_id}")
def remove_student(student_id: int, db: Session= Depends(get_db)):
    student = delete_student(db, student_id)

    if student is None:
        raise HTTPException(status_code= 404, detail="Student not found!")

    return {
        "message":f"'{student.name}' a student has been deleted successfully!"
    }
    
