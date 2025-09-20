# example for odd and even number 

# choice = "y"

# while choice != "n":
#    number = int(input("Enter your number is: "))
#    if number %2 == 0:
#       print(number," is odd number")
#    else:
#       print(number,"is even number") 

#    choice = input("Do want to be continue ? (y/n): ")      
  
#---------------------------------------------------------------------------  

 # mutipale table 

# number = int(input("Enter your number: "))
 
# for i in range(1,11):
#        print(  number ,"X" ,i ,"=",number*i)

#--------------------------------------------------------------------------

#factroial example 

# fact = 4


# for i in range(1,fact):
#     fact=fact*i

# print(fact,"factroial ")

#---------------------------------------------------------------------------

#Fibonacci Series

# fibon = 10
# temp = 0 
# pr = 0
# pe = 1

# for i in range(fibon):
#     temp=pr+pe
#     pr=pe
#     pe=temp

#     print(temp,"fibonacci ")    



#----------------------------------------------------------------------------

#prime number example 

# num  = int(input("Entyer your number is: "))

# flage = 0

# for i in range(2,num):
#     if num %i==0:
#         flage=1
#         break
# if flage==0:
#     print("prime number")
# else:
#     print("Not a prime number")


#-------------------------------------------------------------------------------

#extar example for armstrong number

# number = int(input("Enter your number: "))

# temp = number
# sum = 0

# while number > 0:
#     rem = number % 10
#     sum += rem ** 3    
#     number //= 10

# if sum == temp:
#     print(temp, "is an Armstrong number")
# else:
#     print(temp, "is not an Armstrong number")

# -----------------------------------------------------------------------------

# extar example for pelindron number

# number = int(input("Enter your number: "))

# temp = number
# sum = 0

# while number != 0:
#     rem = number % 10
#     sum = sum * 10 + rem  
#     number = number // 10

# if sum == temp:
#     print(temp, "is a Palindrome number")
# else:
#     print(temp, "is Not a Palindrome number")

# -----------------------------------------------------------------------------


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
#     for k in range(5, i, -1):   
#         print(" ", end=" ")
#     for j in range(1, i+1):     
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


# for i in range(6, 0,-1):      
#     for j in range(6, i, -1):    
#         print(" ", end=" ")
#     for k in range(1, i+1):      
#         print("*", end=" ")
#     print()  

     
#-------------------------------------------------------------------------------------


# for i in range(1,6):
#     for j in range(i):
#         print("*", end="")
#     print()    

# for i in range(6,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()    

# for i in range(1,5):
#     for j in range(1,5):
#         print(" * ",end="")
#     print()    


# for i in range(5,0,-1):
#     for j in range(i):
#         print(" * ",end="")
#     print()    


# for i in range(1,6):
#     for k  in range(5,i,-1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end="")
#     print()


# for i in range(5):
#     for k in range(i):
#         print(" ", end="")
#     for j  in range(4):
#          print(" * ",end="")
#     print()        



# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print() 

# for i in range(5 ,0 ,-1):
#     for j in range(i):
#         print("*",end="")
#     print()    


# ----------------------------------------------------------------------------------------------------------------------------------------------

print("****************************************************")
print("*                                                  *")
print("*           Grade Management System                *")
print("*                                                  *")
print("****************************************************")


def calculate_grade(marks):
    if marks >= 90:
        return "A+ Grade"
    elif marks >= 80:
        return "A Grade"
    elif marks >= 70:
        return "B Grade"
    elif marks >= 60:
        return "C Grade"
    elif marks >= 50:
        return "D Grade"
    elif marks >= 40:
        return "E Grade"
    else:
        return "Fail!"


students = []

choice = "y"

while choice.lower() == "y":
    name = input("Enter your student name: ")
    marks = int(input("Enter your marks (0-100): "))
    
    grade = calculate_grade(marks)
    
 
    students.append({"name": name, "marks": marks, "grade": grade})
    
    choice = input("Do you want to continue? (y/n): ")

print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("All Student Records:")
print("Name\tMarks\tGrade")
for student in students:
    print(f"{student['name']}\t{student['marks']}\t{student['grade']}")



