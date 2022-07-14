from fastapi import APIRouter, status, HTTPException, Body

from src.domain.models.admin_model import AdminSignIn
from src.infrastructure.firebase.authentication.login import admin_exists_query

router = APIRouter()


@router.post("/login()")
def admin_login(admin_credentials: AdminSignIn = Body(...)):
    try:
        return admin_exists_query(admin_credentials.email, admin_credentials.password)

    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())
