import random
import string

def generate_password(length=12):
    # Characters to use
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = uppercase + lowercase + digits + symbols

    # Ensure at least one character from each category
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the remaining length
    for i in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the password
    random.shuffle(password)

    return "".join(password)