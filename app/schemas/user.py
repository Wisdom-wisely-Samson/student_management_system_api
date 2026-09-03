from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)
    role: str = "student"

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool
    role: str


    model_config = {
     "from_attributes": True
      }

class TokenResponse(BaseModel):
    access_token: str
    token_type: str