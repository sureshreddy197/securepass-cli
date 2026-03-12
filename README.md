# SecurePass CLI 🔐

A modular **Python command-line password generator and manager**
designed to generate strong passwords, analyze password strength, and
store generated passwords securely.

This project demonstrates **clean architecture, modular Python design,
CLI tools, logging, and unit testing**, making it a great portfolio
project for Python developers.

------------------------------------------------------------------------

## 🚀 Features

-   Generate **secure random passwords**
-   Password **strength evaluation**
-   CLI-based interaction
-   Modular Python project structure
-   Save generated passwords to file
-   Configurable password rules
-   Logging system for activity tracking
-   Unit testing support

------------------------------------------------------------------------

## 📁 Project Structure

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

------------------------------------------------------------------------

## ⚙️ Requirements

-   Python **3.9+**
-   pip

------------------------------------------------------------------------

## 📥 Installation

Clone the repository:

    git clone https://github.com/sureshreddy197/securepass-cli.git

Move into the project directory:

    cd securepass-cli

(Optional) Create virtual environment:

    python -m venv venv

Activate environment.

Linux / Mac:

    source venv/bin/activate

Windows:

    venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

------------------------------------------------------------------------

## ▶️ Running the Application

Run the CLI tool:

    python main.py

------------------------------------------------------------------------

## 💻 Example Usage

Generate a password:

    python main.py generate --length 16

Example output:

    Generated Password: G8!kL2@pR9#tQ4v
    Strength: Strong

------------------------------------------------------------------------

## 🧪 Running Tests

Run unit tests:

    pytest

Run tests with coverage:

    pytest --cov

------------------------------------------------------------------------

## 🔐 Security

The password generator follows secure practices:

-   Secure random password generation
-   Optional symbol and digit support
-   Password strength evaluation
-   File-based password storage

------------------------------------------------------------------------

## 📚 Technologies Used

-   Python
-   CLI programming
-   File handling
-   Logging
-   Unit testing
-   Modular architecture

------------------------------------------------------------------------

## 🚧 Future Improvements

Possible improvements for this project:

-   GUI version using Tkinter
-   Clipboard copy functionality
-   Password encryption
-   Configuration file support
-   Docker container support
-   API integration

------------------------------------------------------------------------

## 🤝 Contributing

Contributions are welcome.

Steps to contribute:

1.  Fork the repository
2.  Create a feature branch
3.  Commit your changes
4.  Submit a pull request

------------------------------------------------------------------------

## 📄 License

This project is licensed under the MIT License.
