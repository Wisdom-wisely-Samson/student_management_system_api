from fastapi import FastAPI, Request  # type: ignore[import]
from fastapi.responses import JSONResponse
from app.database import Base, engine
from app.routers.student_router import router as student_router
from app.routers.auth_router import router as user_router
from app.config import APP_NAME
from app.loggin_config import setup_logging
from app.exeptions import StudentNotFoundException
from app.exeptions import AppException
import logging
setup_logging()
Base.metadata.create_all(bind= engine)
app = FastAPI(
    title=APP_NAME,
    version="1.1.0"
)
@app.exception_handler(StudentNotFoundException)
async def student_not_found_handler(request: Request, exc: StudentNotFoundException):
    return JSONResponse(status_code=404, content={
        "error": "Student Not Found!",
        "detail": exc.message
    })
logger = logging.getLogger(__name__)
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.exception("Unexpected error occured: %s", exc)
    return JSONResponse(status_code=500, content={
        "error": "Internal Server Error",
        "detail": "Unexpected error occured"
    })

@app.get("/")
def home():
    return {
        "message": "Welcome to the School Management System API!"
    }
@app.exception_handler(AppException)
async def app_exception_handler(
    request: Request,
    exc: AppException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.message
        }
    )




app.include_router(student_router)
app.include_router(user_router)

