from sqlalchemy.orm import Session
from app.models.student import Student
from app.schemas.student import StudentCreate

def get_students(db: Session):
    return db.query(Student).all()

def create_student(db: Session, student: StudentCreate):
    db_student = Student(
        name = student.name,
        age = student.age,
        course = student.course
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student



