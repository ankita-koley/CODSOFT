import random
import string

def generate_password(length=16, use_lowercase=True, use_uppercase=True, use_digits=True, use_special=True):
    # Define characters for each type
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Create a pool of characters to choose from
    characters = ''
    if use_lowercase:
        characters += lowercase_letters
    if use_uppercase:
        characters += uppercase_letters
    if use_digits:
        characters += digits
    if use_special:
        characters += special_characters

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example usage:
password_length = 16
password = generate_password(length=password_length)
print("Generated Password:", password)