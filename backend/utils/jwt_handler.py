import jwt

from datetime import datetime, timedelta

from config import Config


def generate_token(user):

    payload = {
        "username": user["username"],
        "exp": datetime.utcnow() + timedelta(
            hours=Config.JWT_EXPIRE_HOURS
        )
    }

    # Add id only if present
    if "id" in user:
        payload["id"] = user["id"]

    # Add admin flag only if present
    if "is_admin" in user:
        payload["is_admin"] = user["is_admin"]

    return jwt.encode(
        payload,
        Config.SECRET_KEY,
        algorithm="HS256"
    )


def verify_token(token):

    try:

        payload = jwt.decode(
            token,
            Config.SECRET_KEY,
            algorithms=["HS256"]
        )

        return payload

    except jwt.ExpiredSignatureError:
        return None

    except jwt.InvalidTokenError:
        return None