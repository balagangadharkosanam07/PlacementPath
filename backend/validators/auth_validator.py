import re


USERNAME_PATTERN = r"^[A-Za-z0-9_]+$"

EMAIL_PATTERN = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"


def validate_username(username):

    if not username:
        return False, "Username is required."

    if len(username) < 3:
        return False, "Username must be at least 3 characters."

    if len(username) > 30:
        return False, "Username cannot exceed 30 characters."

    if not re.match(USERNAME_PATTERN, username):
        return False, "Username contains invalid characters."

    return True, ""


def validate_email(email):

    if not email:
        return False, "Email is required."

    if not re.match(EMAIL_PATTERN, email):
        return False, "Invalid email address."

    return True, ""


def validate_password(password):

    if not password:
        return False, "Password is required."

    if len(password) < 8:
        return False, "Password must be at least 8 characters."

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."

    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one number."

    return True, ""