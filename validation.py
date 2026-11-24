# Reusable input validation rules (independent of MySQL and Streamlit)
MAX_ID_LENGTH = 50
MAX_NAME_LENGTH = 100


def validate_passenger(passenger_id, first_name, last_name, gender, age, nationality):
    if not isinstance(passenger_id, str) or not passenger_id.strip():
        raise ValueError("Passenger ID cannot be empty.")
    if len(passenger_id.strip()) > MAX_ID_LENGTH:
        raise ValueError("Passenger ID is too long.")

    if not isinstance(first_name, str) or not first_name.strip():
        raise ValueError("First name cannot be empty.")
    if len(first_name.strip()) > MAX_NAME_LENGTH:
        raise ValueError("First name is too long.")

    if not isinstance(last_name, str) or not last_name.strip():
        raise ValueError("Last name cannot be empty.")
    if len(last_name.strip()) > MAX_NAME_LENGTH:
        raise ValueError("Last name is too long.")

    if not isinstance(nationality, str) or not nationality.strip():
        raise ValueError("Nationality cannot be empty.")
    if len(nationality.strip()) > MAX_NAME_LENGTH:
        raise ValueError("Nationality is too long.")

    # type(age) is not int also rejects booleans like True/False
    if type(age) is not int or age < 0 or age > 120:
        raise ValueError("Age must be a whole number between 0 and 120.")

    return (
        passenger_id.strip(),
        first_name.strip(),
        last_name.strip(),
        gender,
        age,
        nationality.strip(),
    )