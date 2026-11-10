import mysql.connector
from dotenv import load_dotenv
import os

def connect_db():
    connection = mysql.connector.connect(
        host=os.getenv("db_host"),
        user=os.getenv("db_user"),
        password=os.getenv("db_password"),
        database=os.getenv("db_database")
    )
    return connection


if __name__ == "__main__":
    load_dotenv()

    try:
        conn = connect_db()

        if conn.is_connected():
            print("Database Connected Successfully!")

        conn.close()

    except Exception as e:
        print("Error:", e)