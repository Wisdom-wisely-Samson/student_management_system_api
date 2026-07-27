from fastapi import FastAPI  # type: ignore[import]
from app.database import Base, engine
from app.models.student import Student
from app.routers.student_router import router as student_router

Base.metadata.create_all(bind= engine)
app = FastAPI(
    title="Student Management API",
    version="1.1.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to the School Management System API!"
    }
app.include_router(student_router)

