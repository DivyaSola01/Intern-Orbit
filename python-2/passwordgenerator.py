import random
import string

def generate_password(length):
    # Define possible characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use random.choices to generate a password of the specified length
    password = ''.join(random.choices(characters, k=length))
    return password

# Prompt user for password length
try:
    length = int(input("Enter the desired length of the password: "))
    if length <= 0:
        print("Please enter a positive number.")
    else:
        password = generate_password(length)
        print(f"\nGenerated Password: {password}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
