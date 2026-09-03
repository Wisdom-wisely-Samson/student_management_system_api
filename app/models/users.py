from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index= True, autoincrement = True)
    username = Column(String, unique = True, nullable = False)
    email = Column(String, unique= True, nullable = False)
    hashed_password = Column(String, nullable = False)
    is_active = Column(Boolean, default = True,)
    role = Column(String, default="student", nullable=False)


