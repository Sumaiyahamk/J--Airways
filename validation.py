MAX_ID_LENGTH = 50
MAX_NAME_LENGTH = 100
MIN_AGE = 0
MAX_AGE = 120


def validate_text(value, field_name, max_length):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} cannot be empty.")
    cleaned = value.strip()
    if len(cleaned) > max_length:
        raise ValueError(f"{field_name} is too long.")
    return cleaned


def validate_passenger(passenger_id, first_name, last_name, gender, age, nationality):
    cleaned_id = validate_text(passenger_id, "Passenger ID", MAX_ID_LENGTH)
    cleaned_first = validate_text(first_name, "First name", MAX_NAME_LENGTH)
    cleaned_last = validate_text(last_name, "Last name", MAX_NAME_LENGTH)
    cleaned_nationality = validate_text(nationality, "Nationality", MAX_NAME_LENGTH)

    if type(age) is not int or age < MIN_AGE or age > MAX_AGE:
        raise ValueError(
            f"Age must be a whole number between {MIN_AGE} and {MAX_AGE}."
        )

    return (
        cleaned_id,
        cleaned_first,
        cleaned_last,
        gender,
        age,
        cleaned_nationality,
    )