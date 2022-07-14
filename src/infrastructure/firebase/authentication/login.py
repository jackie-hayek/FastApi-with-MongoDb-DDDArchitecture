from src.api.auth.jwt_handler import token_response
from src.infrastructure.firebase.configuation.config import auth


def admin_exists_query(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        id_token = user["idToken"]
        return token_response(id_token)

    except:
        raise Exception


def refresh_token():
    return auth.refresh(admin_exists_query.user['refreshToken'])
