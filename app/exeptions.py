class StudentNotFoundException(Exception):
    def __init__(self, student_id: int):
        self.message = f"Student with ID {student_id} was not found."
        super.__init__(self.message)


class AppException(Exception):
    def __init__(
            self,
            message: str,
            status_code: int = 400
    ):
        self.message = message
        self.status_code = status_code

        super().__init__(message)

class NotFoundException(AppException):
    def __init__(self, message: str = "Resource not found"):
        super().__init__(
            message=message,
            status_code=404
        )

class ConflictException(AppException):
    def __init__(self, message: str= "Resource already exist"):
        super().__init__(
            message=message,
            status_code=409
        )