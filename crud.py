from database import connect_db
from validation import validate_passenger


def add_passenger(passenger_id, first_name, last_name, gender, age, nationality):
    passenger_id, first_name, last_name, gender, age, nationality = validate_passenger(
        passenger_id, first_name, last_name, gender, age, nationality
    )

    conn = connect_db()
    cursor = conn.cursor()
    try:
        sql = """
        INSERT INTO Passenger (Passenger_id, First_name, Last_name, Gender, Age, Nationality)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (passenger_id, first_name, last_name, gender, age, nationality))
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()


def get_passengers(limit=20):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        sql = """
        SELECT Passenger_id, First_name, Last_name, Gender, Age, Nationality
        FROM Passenger
        LIMIT %s
        """
        cursor.execute(sql, (limit,))
        rows = cursor.fetchall()
        return rows
    finally:
        cursor.close()
        conn.close()


def update_passenger(passenger_id, age):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        sql = """
        UPDATE Passenger
        SET Age = %s
        WHERE Passenger_id = %s
        """
        cursor.execute(sql, (age, passenger_id))
        if cursor.rowcount == 0:
            raise ValueError("Passenger ID not found.")
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()


def delete_passenger(passenger_id):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM Passenger WHERE Passenger_id = %s"
        cursor.execute(sql, (passenger_id,))
        if cursor.rowcount == 0:
            raise ValueError("Passenger ID not found.")
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()