from database import connect_db


# CREATE
def add_passenger(passenger_id, first_name, last_name, gender, age, nationality):
    """Insert a new passenger record into the Passenger table."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        sql = """
        INSERT INTO Passenger (Passenger_id, First_name, Last_name, Gender, Age, Nationality)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (passenger_id, first_name, last_name, gender, age, nationality))
        conn.commit()
    finally:
        cursor.close()
        conn.close()


# READ
def get_passengers(limit=20):
    """Retrieve a limited number of passenger records from the Passenger table."""
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


# UPDATE
def update_passenger(passenger_id, age):
    """Update the age of an existing passenger by Passenger_id."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        sql = """
        UPDATE Passenger
        SET Age = %s
        WHERE Passenger_id = %s
        """
        cursor.execute(sql, (age, passenger_id))
        conn.commit()
    finally:
        cursor.close()
        conn.close()


# DELETE
def delete_passenger(passenger_id):
    """Delete a passenger record by Passenger_id."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM Passenger WHERE Passenger_id = %s"
        cursor.execute(sql, (passenger_id,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()