from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.models.users import User
from app.auth_dependency import get_current_user, require_role

from app.database import get_db
from app.schemas.user import UserCreate, UserResponse, UserLogin, TokenResponse, StudentRegister, StudentAccountResponse, ChangePassword
from app.services.auth_service import create_user, login_user, create_student_account, change_user_password

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

@router.put("/change-password")
def change_password(
    password_data: ChangePassword,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db), 

):
    success = change_user_password(
        db,
        current_user,
        password_data.current_password,
        password_data.new_password
    )
    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Current password is incorrect"
        )
    return{
        "message": "Password changed successfully!"
    }
@router.put("/{user_id}/deactivate")
def deactivate_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(require_role("admin"))):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    user.is_active = False

    db.commit()
    db.refresh(user)

    return{
        "message": "User deactivated successfully"
    }
@router.put("/{user_id}/activate")
def activate_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(require_role("admin"))):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    user.is_active = True

    db.commit()
    db. refresh(user)

    return{
        "message": "User account activated successfully"
    }
