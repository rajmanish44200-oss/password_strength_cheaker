import string

def check_password(password):
    score = 0

    # Length Check
    if len(password) >= 8:
        score += 2

    # Uppercase Check
    if any(char.isupper() for char in password):
        score += 2

    # Lowercase Check
    if any(char.islower() for char in password):
        score += 2

    # Number Check
    if any(char.isdigit() for char in password):
        score += 2

    # Special Character Check
    if any(char in string.punctuation for char in password):
        score += 2

    # Password Strength
    if score <= 3:
        strength = "Weak"
    elif score <= 6:
        strength = "Medium"
    elif score <= 8:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return score, strength