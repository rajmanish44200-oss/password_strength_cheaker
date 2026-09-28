def get_suggestions(password):
    suggestions = []

    if len(password) < 8:
        suggestions.append("Use at least 8 characters.")
    if not any(c.isupper() for c in password):
        suggestions.append("Add at least one uppercase letter.")
    if not any(c.islower() for c in password):
        suggestions.append("Add at least one lowercase letter.")
    if not any(c.isdigit() for c in password):
        suggestions.append("Add at least one number.")
    if not any(c in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for c in password):
        suggestions.append("Add at least one special character.")

    if not suggestions:
        return "Password is Secure."

    return "\n".join(suggestions)