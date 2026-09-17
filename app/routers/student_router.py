from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.users import User
from app.models.student import Student

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
from app.auth_dependency import get_current_user
from app.auth_dependency import require_role

router = APIRouter(prefix="/students",tags=["Students"])

@router.get("/", response_model=list[StudentResponse])
def read_students(skip: int = Query(default = 0, ge=1, 
    description = "Number of students to skip"),
    limit: int = Query(default = 10, ge = 1, le = 100,
    description = "Maximum number of students to return"),
    db: Session = Depends(get_db), 
    current_user: User = Depends(require_role("admin", "teacher")
)):
    return get_students(db, skip=skip, limit=limit)


@router.post("/", response_model= StudentResponse)
def add_student(student: StudentCreate,
    db: Session = Depends(get_db), 
    current_user: User = Depends(require_role("admin", "teacher"))
):
    return create_student(db, student)
@router.get("/me")
def get_my_student_profile(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    student = (db.query(Student).filter(Student.user_id == current_user.id).first())

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student profile not found!"
        )

    return student

@router.get("/search", response_model=list[StudentResponse])
def search_student(name: str | None = Query(default = None, min_length=1), 
                   course: str | None = Query(default = None, min_length= 1),
                     db: Session = Depends(get_db), current_student: User = Depends(require_role("admin", "teacher"))):
    return search_students(db, name=name, course=course)
# @router.get("/me")
# def get_my_profile()
@router.get("/{student_id}", response_model=StudentResponse)
def read_student(student_id: int, db: Session = Depends(get_db), current_user: User = Depends(require_role("admin", "teacher"))):
    student = get_student_by_id(db, student_id)

    if student is  None:
        raise HTTPException(status_code=404, detail="Student not found!")
    return student
@router.put("/{student_id}", response_model=StudentResponse)
def edit_student(student_id: int, student: StudentUpdate, db: Session = Depends(get_db), current_user: User = Depends(require_role("admin", "teacher")) ):
    updated_student = update_student(db, student_id, student)

    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found!")
    return updated_student
@router.delete("/{student_id}")
def remove_student(student_id: int, db: Session= Depends(get_db), current_user: User = Depends(require_role("admin"))):
    student = delete_student(db, student_id)

    if student is None:
        raise HTTPException(status_code= 404, detail="Student not found!")

    return {
        "message":f"'{student.name}' a student has been deleted successfully!"
    }

@router.put("/{student_id}/link-user/{user_id}")
def link_student_to_user(
    student_id: int,
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("admin"))
):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    if user.role != "student":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only users with student role can be liked"
        )

    student.user_id = user.id

    db.commit()
    db.refresh(student)

    return {
        "message": "Student successfully linked to user",
        "student_id": student.id,
        "user_id": user.id
    }
