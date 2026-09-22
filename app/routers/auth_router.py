from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.models.users import User
from app.auth_dependency import get_current_user

from app.database import get_db
from app.schemas.user import UserCreate, UserResponse, UserLogin, TokenResponse, StudentRegister, StudentAccountResponse
from app.services.auth_service import create_user, login_user, create_student_account

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.post("/register/student", response_model=StudentAccountResponse)
def register_student(student_data: StudentRegister, db: Session = Depends(get_db)):
    new_user, new_student = create_student_account(db, student_data)
    return {
        "message": "Student account created successfully!",
        "user": new_user,
        "student": new_student
    }
@router.get("/me", response_model=UserResponse)
def get_my_profile(db: Session = Depends(get_db), current_user: User =Depends(get_current_user)):
    return current_user

@router.get("/student/me")
def get_my_student_profile(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user.student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student profile not found!"
        )
    return current_user.student

@router.post("/login", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    access_token = login_user(db, form_data.username, form_data.password)

    if not access_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")

    return{
        "access_token": access_token, "token_type": "bearer"
    }