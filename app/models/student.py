from sqlalchemy import Column, Integer, String
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key = True, index = True, autoincrement = True)
    name = Column(String)
    age = Column(Integer)
    course = Column(String)

