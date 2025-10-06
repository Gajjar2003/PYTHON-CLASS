# Simple Calculator

# Perform addition, subtraction, multiplication, division.

# Use functions for each operation.

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


choice = "y"

while choice != "n":

    print("Press 1 is add : ")
    print("Press 2 is sub : ")
    print("Press 3 is mul : ")
    print("Press 4 is div : ")

    option = int(input("Please enter your (+,-,*,/): "))
    
    num1 = int(input("Enter your first number is : "))
    num2 = int(input("Now second number is : "))

    if option == 1:
        print("Result:", add(num1, num2))
    elif option == 2:
        print("Result:", sub(num1, num2))
    elif option == 3:
        print("Result:", mul(num1, num2))
    elif option == 4:
        print("Result:", div(num1, num2))
    else:
        print("Invalid choice! Please try again.")
    
    choice = input("Do you want continue(y/n): ")



