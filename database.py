import os
import mysql.connector
from dotenv import load_dotenv

# Load .env variables immediately when this file is imported
load_dotenv()


def connect_db():
    """Establish and return a connection to the MySQL database."""
    connection = mysql.connector.connect(
        host=os.getenv("db_host"),
        user=os.getenv("db_user"),
        password=os.getenv("db_password"),
        database=os.getenv("db_database"),
    )
    return connection


if __name__ == "__main__":
    try:
        conn = connect_db()
        if conn.is_connected():
            print("Database Connected Successfully!")
        conn.close()
    except Exception as e:
        print("Error:", e)