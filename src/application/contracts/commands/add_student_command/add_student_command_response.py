from beanie import Document
from pydantic import EmailStr


class AddStudentRequestModel(Document):
    student_id: str
    first_name: str
    last_name: str
    enrollment_year: int
    major: str
    email: EmailStr

    class Settings:
        name = "student"

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
