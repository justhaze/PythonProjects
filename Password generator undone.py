import random

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

def generate_password(length):
    # determine how many digits and characters are needed
    digit_count = max(1, length // 3)
    char_count = length - digit_count

    # randomly select digits and characters
    password = []
    for i in range(digit_count):
        password.append(random.choice(DIGITS))
    for i in range(char_count):
        password.append(random.choice(CHARACTERS))

    # add symbols
    if len(password) < length:
        for i in range(length - len(password)):
            password.append(random.choice(SYMBOLS))

    # shuffle the password
    random.shuffle(password)

    # return the password as a string
    return ''.join(password)

# usage example
password_length = int(input("Enter the desired password length: "))
print("Generated password:", generate_password(password_length))
