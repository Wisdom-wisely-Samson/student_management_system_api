from sqlalchemy.orm import Session
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate

def get_students(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Student).offset(skip).limit(limit).all()

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
def get_student_by_id(db: Session, student_id: int):
    return (db.query(Student).filter(Student.id == student_id).first())

def update_student(db: Session, student_id: int, student_data: StudentUpdate):
    student = (db.query(Student).filter(Student.id == student_id).first())

    if student is None:
        return None
    update_data = student_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(student, key, value)
    db.commit()
    db.refresh(student)
    return student 

def delete_student(db: Session, student_id: int):
    student = (db.query(Student).filter(Student.id == student_id).first())

    if student is None:
        return None
    db.delete(student)
    db.commit()
    return student

def search_students(db: Session, name: str | None = None, course: str | None = None):
    query = db.query(Student)

    if name:
        query = query.filter(Student.name.ilike(f"%{name}%"))

    if course:
        query = query.filter(Student.course.ilike(f"%{course}%"))

    return query.all()
