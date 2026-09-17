from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key = True, index = True, autoincrement = True)
    name = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    course = Column(String,nullable=True)
    email = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True
    )
    user = relationship("User", back_populates="student")

