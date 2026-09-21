from pydantic import BaseModel, EmailStr, Field
from app.schemas.student import StudentResponse
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)
    role: str = "student"

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