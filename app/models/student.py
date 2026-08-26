from sqlalchemy import Column, Integer, String
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key = True, index = True, autoincrement = True)
    name = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    course = Column(String,nullable=True)
    email = Column(String, nullable=True)

