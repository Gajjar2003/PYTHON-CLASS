# Day 1 in python praticals
# data-types,variables,opretors,user-inputs

# data-types(int,float,bool)

# int = 12
# float = 12.5
# bool = True

# print(int,float,bool)
# print(type(int),type(float),type(bool))

# user-input data-types

# n = int(input("Enter your number is : "))
# print(n)

# --------------------------------------------data-type end--------------------------------------------------

# Arithmetic Operators

# a = int(input("Enter your number is : "))
# b = int(input("enter your number is : "))

# print("addition is : ",a+b)

# print("Subtraction is : ",a-b)

# print("Multiplication is : ",a*b)

# print("Division is : ",a/b)

# print("Modulus is : ",a%b)

# print("Floor Division is : ",a//b)

# print("Exponentiation is : ",a**b)


# Comparison Operators

# a = int(input("Enter your number is : "))
# b = int(input("enter your number is : "))

# print(a==b)
# print(a<b)
# print(a>b)
# print(a<=b)
# print(a>=b)
# print(a!=b)


# Logical Operators

# a = True
# b = False

# print(a and b)
# print(a or b)
# print(not a)

# Bitwise Operators

# a = int(input("Enter your number is : "))
# b = int(input("enter your number is : "))

# print(a & b )
# print(a | b )
# print(~a)
# print(a >> b )
# print(a << b )


# Assignment Operators


# a = int(input("Enter your number is : "))
# b=a
# print(b)

# b +=a
# print(b)

# b -=a
# print(b)

# b *=a
# print(b)

# b << a
# print(b)


# Identity Operators

# a = 10
# b = 20
# c = a

# print(a is not b)
# print(a is c)

# Membership Operators

# x = 20

# list = [10, 20, 30, 40, 50]

# if(x in list):
#     print("good")
# elif(x not in list):
#     print("error")


# ****************************************************************************************************************************************************************

# Day2 in python praticals
# if , if-else

# age = int(input("Enter your age is : "))

# if(age > 18):
#     print("you are young...")


# if(age >= 18):
#     print("You are young men..")
# else:
#     print("You are child...")






print("Press 1 is multipale table")
print("Press 2 Fibonacci i series is  ")
print("Press 3 is factorial is ")
print("Press 4 is Palindrome number")

option = int(input("Enter your chioce is(1-4): "))


# OPTION 1: Multiplication Table
if option == 1:
    num = int(input("Enter your number: "))

    for i in range(1, 11):
        print(i, "X", num, "=", i * num)


# OPTION 2: Fibonacci Series
elif option == 2: 
    num = int(input("Enter how many Fibonacci numbers you want: "))

    pr = 0
    pe = 1

    print("Fibonacci series:")
    print(pr)
    print(pe)

    for i in range(2, num):
        temp = pr + pe
        pr = pe
        pe = temp
        print(temp)


# OPTION 3: factorial
elif option == 3:
    fact = int(input("Enter your number is: "))

    for i in range(1,fact):
        fact = fact*i

    print(fact)


# OPTION 4: (Palindrome number)
elif option == 4:
    num = input("Enter your number: ")

    if num == num[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")



else:
    print("Invalid choice is...")
 


    
