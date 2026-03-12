# SecurePass CLI

A modular Python command-line password generator with strength analysis, file export, and test coverage.

## Features

- Generate one or many passwords at once
- Choose uppercase, lowercase, numbers, and symbols
- Option to force at least one character from each selected type
- Password strength evaluation
- Save generated passwords to a timestamped text file
- Clean multi-file project structure
- Unit tests included

## Project Structure

```text
securepass-cli/
├── app/
│   ├── __init__.py
│   ├── cli.py
│   ├── config.py
│   ├── generator.py
│   ├── strength.py
│   ├── utils.py
│   └── validator.py
├── tests/
│   ├── __init__.py
│   └── test_generator.py
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## Why this project is good for GitHub

This project looks better than a basic one-file password generator because it has:

- modular code
- input validation
- reusable functions
- tests
- file export
- cleaner architecture

It is still beginner-friendly, but it feels more like a real project.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/sureshreddy197/securepass-cli.git
cd securepass-cli
```

### 2. Run the app

```bash
python main.py
```

## Example Usage

```text
======================
SecurePass CLI v1.0.0
======================
Generate secure passwords with custom rules.
Allowed password length: 8 to 128

Password Settings
-----------------
Enter password length: 14
How many passwords do you want to generate: 3
Include uppercase letters (y/n): y
Include lowercase letters (y/n): y
Include numbers (y/n): y
Include symbols (y/n): y
Force at least one character from each selected type (y/n): y

Generated Passwords
-------------------
1. T4@kLm8!zP2$qR
   Strength: Strong (score: 6/6)
2. pA7#xN4@qZ2!sW
   Strength: Strong (score: 6/6)
3. M8!vY2@rLp5#Qx
   Strength: Strong (score: 6/6)
```

## Running Tests

```bash
python -m unittest discover -s tests
```

## Future Improvements

- Add a GUI using Tkinter or CustomTkinter
- Add clipboard copy support
- Add password history encryption
- Package it as a pip-installable CLI tool
- Add colorized terminal output

## Security Note

This project uses Python's `secrets` module instead of `random` for better password generation security.
