import pymysql
from config import Config


def get_connection():
    """
    Create and return a connection to Amazon RDS MySQL.
    """

    connection = pymysql.connect(
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )

    return connection


def create_tables():
    """
    Create required tables if they do not already exist.
    """

    connection = get_connection()

    try:

        with connection.cursor() as cursor:

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(100) NOT NULL UNIQUE,
                    email VARCHAR(150) NOT NULL UNIQUE,
                    password_hash VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

    finally:

        connection.close()


if __name__ == "__main__":
    create_tables()
    print("Database initialized successfully.")