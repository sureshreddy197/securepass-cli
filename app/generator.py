import secrets
import string

from app.config import SYMBOLS
from app.validator import validate_length, validate_character_pool, validate_count


def build_character_pool(
    use_upper: bool,
    use_lower: bool,
    use_digits: bool,
    use_symbols: bool,
) -> str:
    validate_character_pool(use_upper, use_lower, use_digits, use_symbols)

    pool = ""
    if use_upper:
        pool += string.ascii_uppercase
    if use_lower:
        pool += string.ascii_lowercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += SYMBOLS

    return pool


def generate_password(
    length: int,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    ensure_each_selected_type: bool = True,
) -> str:
    validate_length(length)

    pool = build_character_pool(
        use_upper=use_upper,
        use_lower=use_lower,
        use_digits=use_digits,
        use_symbols=use_symbols,
    )

    required_chars = []

    if ensure_each_selected_type:
        if use_upper:
            required_chars.append(secrets.choice(string.ascii_uppercase))
        if use_lower:
            required_chars.append(secrets.choice(string.ascii_lowercase))
        if use_digits:
            required_chars.append(secrets.choice(string.digits))
        if use_symbols:
            required_chars.append(secrets.choice(SYMBOLS))

        if len(required_chars) > length:
            raise ValueError(
                "Length is too short to include at least one of each selected character type."
            )

    remaining_length = length - len(required_chars)
    password_chars = required_chars + [secrets.choice(pool) for _ in range(remaining_length)]

    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


def generate_multiple_passwords(
    count: int,
    length: int,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    ensure_each_selected_type: bool = True,
) -> list[str]:
    validate_count(count)

    return [
        generate_password(
            length=length,
            use_upper=use_upper,
            use_lower=use_lower,
            use_digits=use_digits,
            use_symbols=use_symbols,
            ensure_each_selected_type=ensure_each_selected_type,
        )
        for _ in range(count)
    ]
