logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""



def add(n1,n2):
    return n1 + n2


def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
'+':add, 
'-':subtract, 
'*':multiply, 
'/':divide
}


def calculator():
    print(logo)
    num1 = float(input("Whats your first number? "))
    continue_game = True
    for symbol in operations:
        print(symbol)
            


    while continue_game: 

        op_symbol = input("What operation would you like to use? ")

        num2 = float(input("Whats your second number? "))

        mathprob = operations[op_symbol]
        first_answer = mathprob(num1,num2)



        mathprob = operations[op_symbol]
        answer = mathprob(num1,num2)


        print(f"{num1} {op_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation? ") == 'y'.lower():
            num1 = answer
        else:
            continue_game == False
            calculator()
calculator()