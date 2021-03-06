from pydantic import EmailStr, BaseModel


class AddStudentResponseModel(BaseModel):
    student_id: str
    first_name: str
    last_name: str
    enrollment_year: int
    major: str
    email: EmailStr

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
