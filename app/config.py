import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL", "sqlite:///./students.db")

APP_NAME = os.getenv("APP_NAME", "Student Management API")

DEBUG = os.getenv("DEBUG", "False").lower() == "true"