import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''

    # Combine all selected characters
    all_characters = lowercase + uppercase + digits + symbols

    if not all_characters:
        raise ValueError("No character sets selected for password generation.")

    # Ensure password includes at least one of each selected type
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_digits:
        password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))

    # Fill remaining characters randomly
    password += random.choices(all_characters, k=length - len(password))

    # Shuffle the password to avoid predictable pattern
    random.shuffle(password)

    return ''.join(password)

# Example usage:
print(generate_password(length=16))  # Generates a strong 16-character password
