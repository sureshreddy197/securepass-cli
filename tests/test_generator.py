import unittest

from app.generator import generate_password, generate_multiple_passwords


class TestPasswordGenerator(unittest.TestCase):
    def test_password_length(self):
        password = generate_password(
            length=12,
            use_upper=True,
            use_lower=True,
            use_digits=True,
            use_symbols=True,
        )
        self.assertEqual(len(password), 12)

    def test_multiple_password_count(self):
        passwords = generate_multiple_passwords(
            count=5,
            length=12,
            use_upper=True,
            use_lower=True,
            use_digits=True,
            use_symbols=False,
        )
        self.assertEqual(len(passwords), 5)

    def test_requires_selected_types(self):
        password = generate_password(
            length=12,
            use_upper=True,
            use_lower=True,
            use_digits=True,
            use_symbols=True,
            ensure_each_selected_type=True,
        )

        self.assertTrue(any(ch.isupper() for ch in password))
        self.assertTrue(any(ch.islower() for ch in password))
        self.assertTrue(any(ch.isdigit() for ch in password))
        self.assertTrue(any(not ch.isalnum() for ch in password))

    def test_invalid_short_length(self):
        with self.assertRaises(ValueError):
            generate_password(length=4)

    def test_invalid_selected_types_combination(self):
        with self.assertRaises(ValueError):
            generate_password(
                length=12,
                use_upper=False,
                use_lower=False,
                use_digits=False,
                use_symbols=False,
            )


if __name__ == "__main__":
    unittest.main()
