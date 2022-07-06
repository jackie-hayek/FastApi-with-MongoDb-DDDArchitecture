from datetime import date
from http.client import HTTPException
from typing import Optional
from pydantic import BaseModel, EmailStr, validator


class UpdateStudentModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    major: Optional[str]
    enrollment_year: Optional[int]

    @validator('enrollment_year')
    def check_enrollment_year(cls, v):
        today_date = date.today()
        current_year = int(today_date.strftime("%Y"))
        if v < current_year:
            raise HTTPException(status_code=400, detail="Invalid Enrollment Year")
        else:
            return v

    class Settings:
        name = "student"

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
