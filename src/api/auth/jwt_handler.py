import time

import jwt


def token_response(token: str):
    return {
        "access_token": token
    }


def decode_token(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, options={"verify_signature": False})
        return decoded_token if decoded_token["exp"] >= time.time() else None
    except:
        return {}
