
import pytest

from crud import add_passenger
from database import connect_db


@pytest.fixture
def test_db(monkeypatch):
    monkeypatch.setenv("db_database", "flight_booking_test")
    conn = connect_db()
    try:
        assert conn.database == "flight_booking_test"
    finally:
        conn.close()


def test_add_passenger(test_db):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        add_passenger("INT01", "Alice", "Smith", "Female", 29, "Finland")

        cursor.execute(
            """
            SELECT Passenger_id, First_name, Last_name, Gender, Age, Nationality
            FROM Passenger
            WHERE Passenger_id = %s
            """,
            ("INT01",),
        )
        result = cursor.fetchone()
        assert result == ("INT01", "Alice", "Smith", "Female", 29, "Finland")
    finally:
        try:
            cursor.execute(
                "DELETE FROM Passenger WHERE Passenger_id = %s",
                ("INT01",),
            )
            conn.commit()
        finally:
            cursor.close()
            conn.close()