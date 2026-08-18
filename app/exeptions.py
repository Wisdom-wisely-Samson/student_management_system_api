class StudentNotFoundException(Exception):
    def __init__(self, student_id: int):
        self.message = f"Student with ID {student_id} was not found."
        super.__init__(self.message)