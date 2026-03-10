# Write a Python program to create a function that takes a string as input and prints it

def hello(text):
    print("You are enter : ",text)

user = input("Enter your string: ")

hello(user)

print("***********************************************************************")

# Write a Python program to create a calculator using functions.

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print("Simple Calculator")
print("Choose operation: +, -, *, /")

choice = input("Enter operation: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "+":
    print("Result:", add(num1, num2))
elif choice == "-":
    print("Result:", sub(num1, num2))
elif choice == "*":
    print("Result:", mul(num1, num2))
elif choice == "/":
    print("Result:", div(num1, num2))
else:
    print("Invalid operation!")


print("***********************************************************************")

# Write a Python program to create a parameterized function that takes two arguments and prints their sum

def add(a, b):
    result = a + b
    print("The sum of", a, "and", b, "is:", result)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

add(num1,num2)


print("***********************************************************************")

# Write a Python program to create a lambda function with one expression

add = lambda a,b:a+b
print("sum = ",add(10,20))

print("***********************************************************************")

# Write a Python program to create a lambda function with two expression

add = lambda a, b: (a + b, a * b)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

sum_result, mul_result = add(x, y)

print("sum : ",sum_result)
print("mul : " , mul_result)