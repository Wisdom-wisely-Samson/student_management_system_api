from app.security import hash_password, verify_password, create_acccess_token
from sqlalchemy.orm import Session
from app.models.users import User



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

    acccess_token = create_acccess_token(data={"sub": str(user.id)})

    return acccess_token