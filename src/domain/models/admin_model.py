from pydantic import BaseModel, EmailStr


class AdminSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "test@youngest.dev",
                "password": "3xt3m#"
            }
        }
