from pathlib import Path
from datetime import datetime


def ask_yes_no(prompt: str) -> bool:
    while True:
        value = input(f"{prompt} (y/n): ").strip().lower()
        if value in {"y", "yes"}:
            return True
        if value in {"n", "no"}:
            return False
        print("Please enter 'y' or 'n'.")


def ask_int(prompt: str, min_value: int | None = None, max_value: int | None = None) -> int:
    while True:
        raw = input(f"{prompt}: ").strip()
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if min_value is not None and value < min_value:
            print(f"Value must be at least {min_value}.")
            continue

        if max_value is not None and value > max_value:
            print(f"Value must be at most {max_value}.")
            continue

        return value


def save_passwords_to_file(passwords: list[str], output_dir: str = "output") -> Path:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = output_path / f"passwords_{timestamp}.txt"

    with file_path.open("w", encoding="utf-8") as file:
        for password in passwords:
            file.write(password + "\n")

    return file_path


def print_header(title: str) -> None:
    line = "=" * len(title)
    print(f"\n{line}\n{title}\n{line}")
