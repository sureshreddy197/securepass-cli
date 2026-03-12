from app.config import APP_NAME, VERSION, DEFAULT_MIN_LENGTH, DEFAULT_MAX_LENGTH, DEFAULT_GENERATE_COUNT
from app.generator import generate_multiple_passwords
from app.strength import evaluate_password_strength
from app.utils import ask_yes_no, ask_int, save_passwords_to_file, print_header


def show_intro() -> None:
    print_header(f"{APP_NAME} v{VERSION}")
    print("Generate secure passwords with custom rules.")
    print(f"Allowed password length: {DEFAULT_MIN_LENGTH} to {DEFAULT_MAX_LENGTH}")


def collect_user_preferences() -> dict:
    print("\nPassword Settings")
    print("-----------------")

    length = ask_int(
        "Enter password length",
        min_value=DEFAULT_MIN_LENGTH,
        max_value=DEFAULT_MAX_LENGTH,
    )

    count = ask_int(
        "How many passwords do you want to generate",
        min_value=1,
        max_value=100,
    )

    use_upper = ask_yes_no("Include uppercase letters")
    use_lower = ask_yes_no("Include lowercase letters")
    use_digits = ask_yes_no("Include numbers")
    use_symbols = ask_yes_no("Include symbols")
    ensure_each_selected_type = ask_yes_no("Force at least one character from each selected type")

    return {
        "length": length,
        "count": count,
        "use_upper": use_upper,
        "use_lower": use_lower,
        "use_digits": use_digits,
        "use_symbols": use_symbols,
        "ensure_each_selected_type": ensure_each_selected_type,
    }


def display_passwords(passwords: list[str]) -> None:
    print("\nGenerated Passwords")
    print("-------------------")

    for index, password in enumerate(passwords, start=1):
        strength_label, score = evaluate_password_strength(password)
        print(f"{index}. {password}")
        print(f"   Strength: {strength_label} (score: {score}/6)")


def run() -> None:
    show_intro()

    while True:
        try:
            preferences = collect_user_preferences()

            passwords = generate_multiple_passwords(
                count=preferences["count"],
                length=preferences["length"],
                use_upper=preferences["use_upper"],
                use_lower=preferences["use_lower"],
                use_digits=preferences["use_digits"],
                use_symbols=preferences["use_symbols"],
                ensure_each_selected_type=preferences["ensure_each_selected_type"],
            )

            display_passwords(passwords)

            if ask_yes_no("\nSave generated passwords to a file"):
                path = save_passwords_to_file(passwords)
                print(f"Saved to: {path}")

        except Exception as exc:
            print(f"\nError: {exc}")

        print("\nOptions")
        print("-------")
        again = ask_yes_no("Generate more passwords")
        if not again:
            print("\nThanks for using SecurePass CLI.")
            break
