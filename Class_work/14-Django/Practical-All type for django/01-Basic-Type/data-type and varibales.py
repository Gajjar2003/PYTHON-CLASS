
# Data type of Pyhton 

a = 10
b = 'Jenil'
c = 12.5
d = True
e = [1,2,3,4,5]
f = (6,7,8,9,10)
g = {11,12,13,14,15}
h = {"name":"jenil"}
i= 2 + 3j

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))


# ------------------------------------------------------------------------------------------------

# Variable in Python

num = 12
_num1 = 12
age = 18
Age = 19
# 1num = 10 use not for vaiable in python
# age@ = 12 use not for vaiable in python

print(num)
print(_num1)
print(age)
print(Age)

# ----------------------------------------------------------------------------------------------

# Opretors in python

# 1.Arithmetic Operators 

a = 4
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b) # value is point value retruns
print(a%b)
print(a**b) # 4*4*4 = 64
print(a//b) # value is not  point value retruns

# 2.Comparison Operators

c = 5
d = 4

print(c == d)
print(c != d)
print(c >= d)
print(c <= d)
print(c > d)
print(c < d)

# Assignment Operators

e = 5
e +=1
print(e)

e = 5
e -=1
print(e)


e = 5
e *=5
print(e)

# Membership Operators
# in and  in not

# Logical Operators
#  and , or, not

# Identity Operators
# is and is not


# ---------------------------------------------------------------------------------------

# statement(if,if-els,if,elfi,switch)

# if statement

age = int(input("Enter your age : "))

if (age >= 18):
    print("You men")


# if-else

num = int(input("Enter your age : "))

if (num > 18):
    print("You are eligible")
else :
    print("You are not eligible")


# if-elfi-else

num = int(input("Enter your num : "))
num1 = int(input("Enter your num : "))
num2 = int(input("Enter your num : "))

if(num > num1 and num > num2):
    print("First num largest")
elif(num1 > num2 and num1 > num):
    print("second num largest")
else:
    print("thrid num largest")


# Switch statement 

print("Press 1 is add :")
print("Press 2 is sub :")
print("Press 3 is mul :")
print("Press 4 is div :")
print("Press 5 is mod :")
print("Press 6 is ** :")
print("Press 7 is // : ")

choice = input("Enter your choice: ")
number = int(input("Enter first number: "))
number1 = int(input("Enter second number: "))

if choice == "1":
    print("Result:", number + number1)

elif choice == "2":
    print("Result:", number - number1)

elif choice == "3":
    print("Result:", number * number1)

elif choice == "4":
    if number1 != 0:
        print("Result:", number / number1)
    else:
        print("Cannot divide by zero")

elif choice == "5":
    print("Result:", number % number1)

elif choice == "6":
    print("Result:", number ** number1)

elif choice == "7":
    print("Result:", number // number1)

else:
    print("Invalid choice")


