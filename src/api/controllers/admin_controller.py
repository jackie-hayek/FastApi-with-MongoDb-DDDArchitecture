from fastapi import APIRouter, status, HTTPException

from src.infrastructure.firebase.authentication.login import admin_exists_query

router = APIRouter()


@router.post("/login/{email, password}", status_code=status.HTTP_200_OK)
def admin_login(email, password):
    try:
        return admin_exists_query(email, password)

    except Exception as e:
        raise HTTPException(status_code=500, detail=e.__str__())