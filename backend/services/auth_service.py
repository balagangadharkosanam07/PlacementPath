from config import Config
from database.db import get_connection
from utils.password import hash_password, verify_password
from utils.jwt_handler import generate_token
from utils.logger import logger

from validators.auth_validator import (
    validate_username,
    validate_email,
    validate_password
)


def register_user(username, email, password):

    if not username or not email or not password:
        return {
            "success": False,
            "message": "All fields are required."
        }

    valid, message = validate_username(username)
    if not valid:
        return {
            "success": False,
            "message": message
        }

    valid, message = validate_email(email)
    if not valid:
        return {
            "success": False,
            "message": message
        }

    valid, message = validate_password(password)
    if not valid:
        return {
            "success": False,
            "message": message
        }

    connection = None

    try:

        connection = get_connection()

        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT * FROM users
                WHERE username = %s OR email = %s
                """,
                (username, email)
            )

            existing_user = cursor.fetchone()

            if existing_user:

                logger.warning(
                    f"Registration failed. Username or Email already exists: {username}"
                )

                return {
                    "success": False,
                    "message": "Username or Email already exists."
                }

            hashed_password = hash_password(password)

            cursor.execute(
                """
                INSERT INTO users
                (username, email, password_hash)
                VALUES (%s, %s, %s)
                """,
                (
                    username,
                    email,
                    hashed_password
                )
            )

        logger.info(
            f"User Registered Successfully: {username}"
        )

        return {
            "success": True,
            "message": "Registration Successful"
        }

    except Exception:

        logger.exception(
            "Unexpected error during registration"
        )

        return {
            "success": False,
            "message": "Something went wrong."
        }

    finally:

        if connection:
            connection.close()


def login_user(username, password):

    if not username or not password:
        return {
            "success": False,
            "message": "Username and Password are required."
        }

    valid, message = validate_username(username)
    if not valid:
        return {
            "success": False,
            "message": message
        }

    connection = None

    try:

        connection = get_connection()

        with connection.cursor() as cursor:

            cursor.execute(
                """
                SELECT *
                FROM users
                WHERE username = %s
                """,
                (username,)
            )

            user = cursor.fetchone()

            if not user:

                logger.warning(
                    f"Login failed. User not found: {username}"
                )

                return {
                    "success": False,
                    "message": "Invalid username or password."
                }

            if not verify_password(password, user["password_hash"]):

                logger.warning(
                    f"Invalid password for user: {username}"
                )

                return {
                    "success": False,
                    "message": "Invalid username or password."
                }

            token = generate_token(user)

            logger.info(
                f"User Logged In Successfully: {username}"
            )

            return {
                "success": True,
                "message": "Login Successful",
                "token": token,
                "user": {
                    "id": user["id"],
                    "username": user["username"],
                    "email": user["email"]
                }
            }

    except Exception:

        logger.exception(
            "Unexpected error during login"
        )

        return {
            "success": False,
            "message": "Something went wrong."
        }

    finally:

        if connection:
            connection.close()


def get_all_users():

    connection = None

    try:

        connection = get_connection()

        with connection.cursor() as cursor:

            cursor.execute("""
                SELECT
                    id,
                    username,
                    email,
                    created_at
                FROM users
                ORDER BY id DESC
            """)

            users = cursor.fetchall()

        user_list = []

        for user in users:

            user_list.append({

                "id": user["id"],

                "username": user["username"],

                "email": user["email"],

                "created_at": str(user["created_at"])

            })

        logger.info("Admin viewed all users.")

        return {
            "success": True,
            "users": user_list
        }

    except Exception:

        logger.exception(
            "Error fetching users."
        )

        return {
            "success": False,
            "message": "Unable to fetch users."
        }

    finally:

        if connection:
            connection.close()


def admin_login(username, password):

    if (
        username == Config.ADMIN_USERNAME
        and password == Config.ADMIN_PASSWORD
    ):

        token = generate_token({
            "username": username,
            "is_admin": True
        })

        logger.info("Admin Logged In Successfully")

        return {
            "success": True,
            "message": "Admin Login Successful",
            "token": token
        }

    logger.warning("Invalid Admin Login Attempt")

    return {
        "success": False,
        "message": "Invalid Admin Credentials"
    }
