import random

#list of items
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
 
CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
 
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
    


password = []

char_amount = int(input("How many chars do you want to use? "))

for nums in range(1, char_amount + 1):
    randdigits = random.choice(DIGITS)
    password += randdigits
print(password)

# symbol_ammount = input("How many symbols do you want to use? ")

# password_length = digit_amount + char_amount + symbol_ammount


