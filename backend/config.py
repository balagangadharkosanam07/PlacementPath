import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Config:

    # Flask Configuration
    SECRET_KEY = os.getenv("SECRET_KEY")

    # Amazon RDS (MySQL) Configuration
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = int(os.getenv("DB_PORT", 3306))
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    # JWT Configuration
    JWT_EXPIRE_HOURS = int(
        os.getenv("JWT_EXPIRE_HOURS", 2)
    )

    # Default Admin Credentials
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")