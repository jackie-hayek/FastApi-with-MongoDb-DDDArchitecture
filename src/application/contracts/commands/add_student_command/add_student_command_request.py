import re
import uuid
from datetime import date

from pydantic import validator, EmailStr, BaseModel


class AddStudentRequestModel(BaseModel):
    student_id: str = str(uuid.uuid4())
    first_name: str
    last_name: str
    enrollment_year: int
    major: str
    email: EmailStr

    @validator('email')
    def check_email_format(cls, v):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, v):
            return v
        else:
            raise ValueError("Email is not valid")

    @validator('enrollment_year')
    def check_enrollment_year(cls, v):
        today_date = date.today()
        current_year = int(today_date.strftime("%Y"))
        if v < current_year:
            raise ValueError("Enrollment year is not valid")
        else:
            return v

    class Settings:
        name = "student"

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
