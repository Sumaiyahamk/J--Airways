import pytest
from validation import validate_passenger


def test_valid_passenger_is_cleaned():
    # Arrange
    raw_id = "  P1001  "
    raw_first = "  Alice "
    raw_last = " Smith  "
    raw_gender = "Female"
    raw_age = 29
    raw_nationality = "  Finland "

    # Act
    result = validate_passenger(
        raw_id, raw_first, raw_last, raw_gender, raw_age, raw_nationality
    )

    # Assert
    assert result == ("P1001", "Alice", "Smith", "Female", 29, "Finland")


def test_empty_passenger_id_is_rejected():
    with pytest.raises(ValueError, match="Passenger ID cannot be empty"):
        validate_passenger("", "Alice", "Smith", "Female", 29, "Finland")


def test_spaces_only_first_name_is_rejected():
    with pytest.raises(ValueError, match="First name cannot be empty"):
        validate_passenger("P1001", "   ", "Smith", "Female", 29, "Finland")


def test_too_long_first_name_is_rejected():
    long_name = "A" * 101
    with pytest.raises(ValueError, match="First name is too long"):
        validate_passenger("P1001", long_name, "Smith", "Female", 29, "Finland")


@pytest.mark.parametrize("invalid_age", [-1, 121, 25.5, "30", True])
def test_invalid_age_is_rejected(invalid_age):
    with pytest.raises(ValueError, match="Age must be a whole number"):
        validate_passenger("P1001", "Alice", "Smith", "Female", invalid_age, "Finland")


def test_boundary_ages_are_accepted():
    result_min = validate_passenger("P1001", "Alice", "Smith", "Female", 0, "Finland")
    result_max = validate_passenger("P1001", "Alice", "Smith", "Female", 120, "Finland")

    assert result_min[4] == 0
    assert result_max[4] == 120