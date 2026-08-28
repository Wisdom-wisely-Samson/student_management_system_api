from app.security import hash_password
from sqlalchemy.orm import Session
from app.models.users import User



def create_user(db: Session, user_data):
    hashed_password = hash_password(user_data.password)
    
    new_user = User(
        username = user_data.username,
        email = user_data.email,
        hashed_password = hashed_password
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
