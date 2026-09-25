from pydantic import BaseModel, EmailStr, Field
from app.schemas.student import StudentResponse
from typing import Literal
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)

    model_config = {
        "extra": "forbid"
    }

class StudentRegister(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)

    name: str
    age: int
    course: str

    
class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool
    role: str

class StudentAccountResponse(BaseModel):
    message: str
    user: UserResponse
    student: StudentResponse


    model_config = {
     "from_attributes": True
      }

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class ChangePassword(BaseModel):
    current_password: str
    new_password: str = Field(min_length=8, max_length=72)

class RoleUpdate(BaseModel):
    role: Literal["student", "teacher", "admin"]