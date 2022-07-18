from pydantic import BaseModel, EmailStr


class Student(BaseModel):
    student_id: str
    first_name: str
    last_name: str
    enrollment_year: str
    major: str
    email: EmailStr

    class Config:
        orm_mode = True

