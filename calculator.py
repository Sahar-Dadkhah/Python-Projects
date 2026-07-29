from replit import clear
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

logo=r"""
 _____________________
|  _________________  |
| | Pythonista 0.   | |
| |_________________| |
|  ___ ___ ___ ___  | |
| | 7 | 8 | 9 | + | | |
| |___|___|___|___| | |
| | 4 | 5 | 6 | - | | |
| |___|___|___|___| | |
| | 1 | 2 | 3 | x | | |
| |___|___|___|___| | |
| | . | 0 | = | / | | |
| |___|___|___|___| | |
|_____________________|
"""
 
calc_dictionary={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
def calculator():
    print(logo,"\n")
    print("Welcome to the Python Calculator !")
    num1=float(input("What's the first number?: "))

    for operation in calc_dictionary:
        print(operation)
    should_continue=True
    while should_continue:

        operation=input("Pick an operation: ")
        num2=float(input("What's the next number?: "))
        calculation=calc_dictionary[operation]
        answer=calculation(num1,num2)
        print (f"{num1}{operation}{num2}={answer}")
        if input(f"Type \'y' to continue calculating with {answer} or \'n' to start a new calculation : ")=="y":
            num1=answer
        else:
            should_continue=False
            clear()

            calculator()
calculator()

input("")