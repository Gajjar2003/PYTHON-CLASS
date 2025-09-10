# Write a Python program to check if a number is positive or negative
# number = int(input("Enter your number is:- "))

# if number > 0:
#     print("Number is positive")
# else:
#     print("number is negative") 


# Write a program to check whether a person is eligible to vote or not.

# number = int(input("Enter your number is:- "))

# if number >= 18:
#     print("You are eligible")
# else:
#     print("You arte not eilgible")

# Write a program to find the greatest of two numbers.

# number = int(input("Enter your fisrt number is:- "))
# number1 =  int(input("Enter your second number is:- "))

# if number > number1:
#     print("First number is greatset")
# else:
#     print("second number is greatest")

# Write a program to check whether a given number is even or odd.

# number = int(input("Enter your number is:- "))

# if  number %2 == 0:
#     print("Number is even")
# else:
#     print("number is odd") 

# Write a program to check whether a given year is a leap year or no

# number = int(input("Enter your years is:- "))

# if  number %4 == 0:
#     print("leep years")
# else:
#     print("Not leep yaers") 


# Write a program to check whether a character is a vowel or consonant.

# char = input("Enter your character:- ")

# if char in ['a', 'e', 'i', 'o', 'u']:
#     print("Enter your character is vowel")
# else:
#     print("Enter your character is consonant")


# Write a program to check if a given number is divisible by 5 or not.

# number = int(input("Enter your number is:- "))

# if  number %5 == 0:
#     print("divisible ")
# else:
#     print("Not divisible") 

# Write a program to check whether a student has passed or failed (marks >= 35 is pass)

# number = int(input("Enter your number is:- "))

# if number >= 35:
#     print("You  are pass")
# else:
#     print("you are Fail")

# Write a program to check whether a given string is empty or not.



# s = input("Enter a string: ")

# if s == "":
#     print("The string is empty")
# else:
#     print("The string is not empty")

# ------------------------------------------------------------------ladder if–else----------------------------------------------------------------------

# Write a program to check whether a number is positive, negative, or zero.

# num = int(input("Enter your number is:- "))

# if  num > 0:
#     print("number is postive ")
# elif num < 0:
#     print("number is negative")
# else:
#     print("number is zero")


# Write a program to find the greatest of three numbers.

# num1 = int(input("Enter your fisrt number is:- "))
# num2 =  int(input("Enter your second number is:- "))
# num3 = int(input("Enter your three number is: -"))

# if num1 > num2 and num1 > num3:
#     print("first number is greatest")
# elif num2 > num1 and num2 > num3:
#     print("second number is greatest")
# else:
#     print("thrid number is greatest ")

# Write a program to check the grade of a student based on marks:

# 90 and above → A

# 75–89 → B

# 50–74 → C

# 35–49 → D

# Below 35 → Fail

# marks = int(input("Enter your marks:- "))

# if marks >= 90:
#     print("A+ grade")
# elif marks > 80:
#     print("A grade")
# elif marks > 70:
#     print("B grade")
# elif marks > 50:
#     print("C grade")
# elif marks > 40:
#     print("D garde")
# elif marks > 35:
#     print("Just pass")
# else:
#     print("Fail !")


# Write a program to check whether a given year is a leap year, century year, or not a leap year

# year = int(input("Enter a year: "))

# if year % 400 == 0:
#     print(year, "is a leap year (century year)")
# elif year % 100 == 0:
#     print(year, "is a century year but not a leap year")
# elif year % 4 == 0:
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")


# Write a program to display the day of the week (1 = Monday, 2 = Tuesday, …, 7 = Sunday).


# Program to display the day of the week

# day = int(input("Enter a number (1-7): "))

# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("Invalid input! Please enter a number between 1 and 7.")

# Write a program to classify a character as vowel, consonant, digit, or special character.

# ch = input("Enter your single character:- ")

# if  ch.isdigit():
#     print(" digit")
# elif ch.lower() in ['a', 'e', 'i', 'o', 'u']:
#     print("vowel")
# elif ch.isalpha():
#     print("consonant")
# else:
#     print("special")
