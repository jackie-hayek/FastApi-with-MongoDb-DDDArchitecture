from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.api.auth.jwt_handler import decode_token
from src.infrastructure.firebase.authentication.login import refresh_token


def verify_jwt(jwtoken: str) -> bool:
    isTokenValid: bool = False

    payload = decode_token(jwtoken)
    if payload:
        isTokenValid = True
    if None:
        refresh_token()
    return isTokenValid


class JWTBearer(HTTPBearer):

    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        print("Credentials :", credentials)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication token")

            if not verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token")

            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization token")