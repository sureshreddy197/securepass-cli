from app.config import DEFAULT_MIN_LENGTH, DEFAULT_MAX_LENGTH


def validate_length(length: int) -> None:
    if not isinstance(length, int):
        raise TypeError("Password length must be an integer.")

    if length < DEFAULT_MIN_LENGTH:
        raise ValueError(f"Password length must be at least {DEFAULT_MIN_LENGTH}.")

    if length > DEFAULT_MAX_LENGTH:
        raise ValueError(f"Password length must not exceed {DEFAULT_MAX_LENGTH}.")


def validate_character_pool(
    use_upper: bool,
    use_lower: bool,
    use_digits: bool,
    use_symbols: bool,
) -> None:
    if not any([use_upper, use_lower, use_digits, use_symbols]):
        raise ValueError("At least one character type must be selected.")


def validate_count(count: int) -> None:
    if not isinstance(count, int):
        raise TypeError("Count must be an integer.")
    if count < 1:
        raise ValueError("Count must be at least 1.")
    if count > 100:
        raise ValueError("Count must not exceed 100.")
