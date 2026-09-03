from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.users import User

from app.config import SECRET_KEY, ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
          detail="Could not validate credentials", 
          headers={"WWW-Authentication": "Bearer"}
    )

    try:
        payload = jwt.decode(
            token, SECRET_KEY, algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        if user_id is None:
            raise credential_exception

        user = db.query(User).filter(User.id == int(user_id)).first()
        
        if user is None:
            raise credential_exception
        return user
    except JWTError:
        raise credential_exception

def require_role(required_role: str):
    def role_checker(current_user: User = Depends(get_current_user)):

        if current_user.role not in required_role:

            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't have permission to perform this action"
            )

        return current_user
    return role_checker