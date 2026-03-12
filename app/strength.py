def evaluate_password_strength(password: str) -> tuple[str, int]:
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(ch.islower() for ch in password):
        score += 1
    if any(ch.isupper() for ch in password):
        score += 1
    if any(ch.isdigit() for ch in password):
        score += 1
    if any(not ch.isalnum() for ch in password):
        score += 1

    if score <= 2:
        return "Weak", score
    if score <= 4:
        return "Medium", score
    return "Strong", score
