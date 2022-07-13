from src.infrastructure.firebase.configuation.config import auth


def admin_exists_query(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        id_token = user["idToken"]
        return id_token

    except:
        raise Exception

