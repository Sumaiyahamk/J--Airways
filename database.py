import mysql.connector

def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="7862492",
        database="airline_booking"
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