from app.security import hash_password, verify_password, create_access_token
from sqlalchemy.orm import Session
from app.models.users import User
from app.models.student import Student



def create_user(db: Session, user_data):
    hashed_password = hash_password(user_data.password)
    
    new_user = User(
        username = user_data.username,
        email = user_data.email,
        hashed_password = hashed_password,
        role =user_data.role
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def create_student_account(db: Session, student_data):
    hashed_password = hash_password(student_data.password)

    new_user = User(
        username = student_data.username,
        email=student_data.email,
        hashed_password= hashed_password,
        role="student"
    )
    db.add(new_user)
    db.flush()

    new_student = Student(
    name=student_data.name,
    age=student_data.age,
    course=student_data.course,
    email=student_data.email,
    user_id=new_user.id
)

    db.add(new_student)
    db.commit()
    db.refresh(new_user)
    db.refresh(new_student)

    return new_user, new_student

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user

def login_user(db: Session, username: str, password: str):
    user = authenticate_user(db, username, password)

    if not user:
        return None

    access_token = create_access_token(data={"sub": str(user.id)})

    return access_token