from database import connect_db

def add_passenger(first_name, last_name, age):
    conn = connect_db()
    cursor = conn.cursor()

    sql = """
    INSERT INTO Passenger(first_name, last_name, age)
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (first_name, last_name, age))
    conn.commit()

    print("Passenger Added Successfully")

    cursor.close()
    conn.close()


def get_passengers():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Passenger")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()

    from database import connect_db

# CREATE
def add_passenger(first_name, last_name, age):
    conn = connect_db()
    cursor = conn.cursor()

    sql = """
    INSERT INTO Passenger(first_name, last_name, age)
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (first_name, last_name, age))
    conn.commit()

    print("Passenger Added Successfully")

    cursor.close()
    conn.close()


# READ
def get_passengers():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Passenger")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()


# UPDATE
def update_passenger(passenger_id, age):
    conn = connect_db()
    cursor = conn.cursor()

    sql = """
    UPDATE Passenger
    SET age = %s
    WHERE passenger_id = %s
    """

    cursor.execute(sql, (age, passenger_id))
    conn.commit()

    print("Passenger Updated Successfully")

    cursor.close()
    conn.close()


# DELETE
def delete_passenger(passenger_id):
    conn = connect_db()
    cursor = conn.cursor()

    sql = """
    DELETE FROM Passenger
    WHERE passenger_id = %s
    """

    cursor.execute(sql, (passenger_id,))
    conn.commit()

    print("Passenger Deleted Successfully")

    cursor.close()
    conn.close()