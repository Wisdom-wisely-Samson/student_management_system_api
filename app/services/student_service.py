from sqlalchemy.orm import Session
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate
import logging
from app.exeptions import StudentNotFoundException

logger = logging.getLogger(__name__)

def get_students(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Student).offset(skip).limit(limit).all()

def create_student(db: Session, student: StudentCreate):
    try:
        db_student = Student(
                name = student.name,
                age = student.age,
                course = student.course
            )
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        logger.info("Student created: id=%s name=%s", db_student.id, db_student.name)
                
        return db_student

    except Exception:
        db.rollback()

        logger.exception(
            "Failed to create student"
        )


def get_student_by_id(
    db: Session,
    student_id: int
):
    student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )

    if not student:
        logger.info(
                    "Student not found: id=%s", student_id
                )
        raise StudentNotFoundException
    
    logger.info(
            "Student found: id=%s", student_id
        )
    return student
    
        
    


def update_student(db: Session, student_id: int, student_data: StudentUpdate):
    try:

        student = (db.query(Student).filter(Student.id == student_id).first())

        if not student:
          logger.info("Student not found!")
          raise StudentNotFoundException
        update_data = student_data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
         setattr(student, key, value)
        db.commit()
        logger.info("Student updated: id=%s", student_id)
        db.refresh(student)
        return student 

    except Exception:
        db.rollback()
        logger.exception("Failed to update Student")
def delete_student(db: Session, student_id: int):
    try:
        student = (db.query(Student).filter(Student.id == student_id).first())

        if not student:
         logger.info("Student not found!")
         raise StudentNotFoundException
    
    
        db.delete(student)
        db.commit()
        logger.info("Student deleted: id=%s", student_id)
        return student
    except Exception:
        db.rollback()
        logger.exception(
            "Delete Failed"
        )

def search_students(db: Session, name: str | None = None, course: str | None = None):
    query = db.query(Student)

    if name:
        query = query.filter(Student.name.ilike(f"%{name}%"))
        logger.info(f"Found {name}(s)!")

    if course:
        query = query.filter(Student.course.ilike(f"%{course}%"))
        logger.info(f"Course(s) Found")
    
    results = query.all()

    if not results:
        logger.warning("No matches found for the search criteria")
        raise StudentNotFoundException
    return results
