# extra example foe if-else statement
# student marks sheet program

# print("------Student marks program--------")

# marks = int(input("Please enter your marks is: "))

# if marks > 90:
#     print("You are A grade")
# elif marks < 90 and marks > 85:
#     print("You are B grade")    
# elif marks < 80 and  marks > 70:
#     print("You are C garde")
# elif marks < 70 and marks > 50:
#     print("You are D grade")
# else:
#     print("You are fail it !")

# **********************************************************************************************

#extra example for looping statement 
#student marks sheet program

# print("****** student marks *******")

# choice = "y"
# while choice != "n":
#     marks = int(input("Please enter your marks : "))
#     if marks > 90 and marks < 100:
#         print("Your are A+ grade ")
#     elif marks > 80  and marks < 90:
#         print("You are A garde")
#     elif marks > 70 and marks < 80:
#         print("You are B garde")
#     elif marks > 60 and marks < 70:
#         print("You are C garde ")
#     elif marks > 50 and marks < 60:
#         print("You are D garde ")
#     elif marks > 30 and marks < 40:
#         print("You are pass")
#     else:
#         print("You are fail") 

#     choice = input("Do you want continue ? (y/n): ")

#---------------------------------------------------------------------------------------------------

#extra example for prime number check

# number = 11
# flage = 0 

# for i in range(2,number):
#     if number%i==0:
#        flage=1
#        break
# if flage == 0 :
#     print(number,"is prime number")
# else:
#     print(number, "is not prime number")        
    

# for j in range(3,400):
#     number = j
#     flage = 0 

#     for i in range(3,number):
#         if number %i==0:
#             flage=1
#             break
#     if flage == 0 :
#         print(number,"is prime number")
#     else:
#         pass    


#----------------------------------------------------------------------------------------------------


# *
# * * 
# * * *
# * * * *
# * * * * *

# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()    


# -------------------------------------------------------------------------------

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *


# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end="")
#     print()


# -------------------------------------------------------------------------------


# * * * * *
# * * * *
# * * *
# * *
# *


# for i in range(5 ,0 ,-1):
#     for j in range(i):
#         print("*",end="")
#     print()    

#---------------------------------------------------------------------------------

    #            *
    #          * *
    #        * * *
    #      * * * *
    #    * * * * * 


# for i in range(1, 6):       
#     for j in range(5, i, -1):   
#         print(" ", end=" ")
#     for k in range(1, i+1):     
#         print("*", end=" ")
#     print()   
 

# for i in range(1, 6):   
#     print("  " * (5 - i), end="")   
#     print("* " * i)     


# ----------------------------------------------------------------------------------

#   * * * * *
#     * * * *
#       * * *
#         * *
#           *


# for i in range(6, 0, -1):      
#     for j in range(6, i, -1):    
#         print(" ", end=" ")
#     for k in range(1, i+1):      
#         print("*", end=" ")
#     print()  


# write a program find min and max number use to function reduce ()


# from functools import reduce

# l = [12,771,8474,1,74,2345,74887,4544]

# def max(a,b):
#     if a > b:
#         return a
#     else :
#         return b 
    
# maxmum = reduce(max,l)    
# print(maxmum)

# def min(a,b):
#     if a < b :
#         return a
#     else :
#         return b

# minmum = reduce(min,l)
# print(minmum)


# write a program to avg use to reduce function


# from functools import reduce

# l = [12, 771, 8474, 1, 74, 2345, 74887, 4544]
# total = reduce(lambda a, b: a + b, l)
# average = total / len(l)
# print("Average:", average)

  

#  write a program to perfect sqaure in filter function

# import math
# l = [1,2,3,4,5,6,7,8,9,25,49]
# def check_p_square(a):
#     if math.sqrt(a).is_integer():
#         return a

# k = filter(check_p_square,l)
# k = filter(lambda a : math.sqrt(a).is_integer(),l)
# print(list(k))



# di = {
#     "name" : "jenil",
#     "age" : 21,
#     "email" : "jenil@gamil.com"
# }

# di["name"]= "ravi"
# print(di)
# di.update({"subject": "python"})
# print(di)
# print(di["name"][0])


# d = {"name": "om",
#      "Age" : 21
     
#     }

# d["name"]= "meet"
# print(d)

# # d.update({"email" : "j@gamil.com"})
# print(d)


# def test(func):
#     def wrapper():
#         func()  
#         print("testing...") 
#     return wrapper

# @test
# def demo():
#     print("testing for demo......")

# demo()


# class student:
#     name = "jenil"
#     age = 21
#     email = "je@g ail.com"

#     def display(self):
#         print(self.name,self.age,self.email)


# s = student()
# s.display()
# s.email = "jenil@gamil.com"
# s.display()


# class employee:
#     def __init__(self,id,name,email,department):
#         self.id= id
#         self.name = name
#         self.email = email
#         self. departement = department

#     def display(self):
#         print("Emplyoee infromation")
#         print(self.id,self.name,self.email,self.departement)
        

# e = employee(1, "jenil","emila@hamil.com","marketing ")
# e.display()



# *******************************************************************************************************

# print("hello world!")


# Write a program to swap two numbers.

# a = 10 
# b = 20
# temp =a
# a= b
# b =temp

# print(a,b)


# Write a program to find the area of a circle.

# r = int(input("Enter your circle of area : "))

# total = r*r
# print("total area of circle is: ",total)


# Write a program to convert Celsius to Fahrenheit.

# cel = int(input("Enter your celcius: "))

# f = (cel*1.8)+32

# print("fahrenheit",f)


# 
# Write a program to calculate the simple interest.

# p = int(input("Enter your priciple : "))
# r = int(input("Enter your rate: "))
# t = int(input("Entert your time: "))

# simple = (p*r*t) / 100

# print(simple)



def only_number(num):
    def wrapper(*a):
        if not str(a[0]).isdigit():
            print("Only number values are allowed!")
        else:
            num(*a)
    return wrapper

@only_number
def num(a):
    print("Number:", a)


num(10)      
num("abc") 


def only_character(ch):
    def wapper(*a):
        if not str(a[0]).isalpha():
            print("only character values are allowed!")
        else:
            ch(*a)
    return wapper

@only_character
def ch(a):
    print("character",a)

ch(10)
ch("j")


def only_sp(sp):
    def wapper(*a):
        if  str(a[0]).isalnum():
            print("only sp value are allowed!")
        else:
            sp(*a)
    return wapper

@only_sp
def sp(*a):
    print("spe",a)



sp(10)
sp("j")
sp("@")