import random
import string

def generate_random_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    """
    Generate a random password with the specified length and options.

    :param length: The length of the password (default is 12)
    :param use_uppercase: Whether to include uppercase letters (default is True)
    :param use_digits: Whether to include digits (default is True)
    :param use_special_chars: Whether to include special characters (default is True)
    :return: A randomly generated password
    """
    # Define possible characters
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Build the character pool based on the options provided
    char_pool = lower_case
    if use_uppercase:
        char_pool += upper_case
    if use_digits:
        char_pool += digits
    if use_special_chars:
        char_pool += special_chars

    # Generate a random password from the character pool
    password = ''.join(random.choice(char_pool) for _ in range(length))

    return password

# Example Usage
password = generate_random_password(length=16, use_uppercase=True, use_digits=True, use_special_chars=True)
print(f"Generated Random Password: {password}")
