from pydantic import BaseModel, Field

class StudentCreate(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(gt=0, lt=100)
    course: str = Field(min_length=3)

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    course: str

model_config = {
"from atributes": True
}

    