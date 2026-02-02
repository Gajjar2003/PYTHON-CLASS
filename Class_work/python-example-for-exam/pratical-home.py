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


# -------------------------------------------------------------------------------------------------------------

# Pyhton variables

# a = 10
# v = 20
# print(a)
# print(v)

# ---------------------------------------------------------------------------------------------------------

# Python Datatypes (int,str, float,boolean)

# n = 10
# n1 = "jenil"
# n2 = 12.5
# n3 = True
# print(type(n))
# print(type(n1))
# print(type(n2))
# print(type(n3))

# import random

# print(random.randrange(1, 10))


# ----------------------------------------------------------------------------------------------------

# Python Data type and varivables

num = 10
num1 = "Jenil"
num2 = 12.5
num3 = True

print(type(num))
print(type(num1))
print(type(num2))
print(type(num3))

#Python oprators

a = 4
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)

c = 5 
d = 5

print(c == d)
print(c != d)
print(c >= d)
print(c <= d)

e = 1
e +=5
e-=5
print(e)

f = 5
f *= 5
print(f)

# if and else 


age  = 22

if (age > 18):
    print("you young")

else : 
    print("You are chalid")



# loop for and while loop

h = 15

for i in range(1,11):
    print(i,"X",h,"=",i*h)


n = 5

for i in range(1,n):
    n = n*i

    print(n)


f = 5
temp = 0
pr = 0
pe = 1

print(pr)
print(pe)
for i in range(f):
    temp = pr+pe
    pr=pe
    pe=temp

    print(temp)



num = 121
num_str = str(num)

if num_str == num_str[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")



l = 151
flag = 0

for i in range(2, l):
    if l % i == 0:  
        flag = 1
        break

if flag == 0:
    print("Prime")
else:
    print("Not Prime")


# string

s = "jenil1"
print(len(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.casefold())
print(s.title())
print(s.strip())
print(s.split())
print(s.startswith("j"))
print(s.endswith("l"))
print(s.find("e"))
print(s.join("gajjar"))
print(s.zfill(10))
print(s.isdigit())
print(s.isalpha())
print(s.replace("j","g"))


# list

l = [1,2,3,4,5,6,7,8,9,10]
l1= [14,15,16]
print(len(l))
print(type(l))
print(l)
print(l[3])
print(l[2:6])
l.append(11)
print(l)
l.insert(0,0)
print(l)
l.sort()
print(l)
l.count(4)
print(l)
l2 = l+l1
print(l2)

t = (11,12,13,14,15,16)


print(len(t))
print(type(t))

l= list(t)
l.append("17")
print(tuple(l))


s = {1,2,3,4,5,6,7,8,9,10}

s1 = {10,12,13,14,15,16,17,18,19,20}


print(type(s))
print(len(s))
s.add(11)
print(s)
s.update([1,11])
print(s)

s3 = s.union(s1)
print(s3)

s4 = s.intersection(s1)
print(s4)

s5 = s.symmetric_difference(s1)
print(s5)

s6 = s.isdisjoint(s1)
print(s5)

s7 = s.issubset(s1)
print(s7)

s8 = s.issuperset(s1)
print(s8)



d = {
    "name":"jenil",
    age : 24,
    "email": "jenil@gamio.com"
}


print(len(d))
print(type(d))
print(d.keys())
print(d.values())
print(d.get("name"))
print(d.items())
d["gajjar"]= "jenil"
print(d)



# # Fuction

# def add():
#     b = a*a
#     print(b)

# add(8)



class pen :
    price = 10
    name = "cello"
    color = "red"

    def display(self):
        print(self.price,self.name,self.color)

class notbook(pen):
    pages = 50 

    def show(self):
        self.price = 20
        print(self.price,self.name,self.color,self.pages)


p = pen()
p.display()

n = notbook()
n.show()


class clg:
    
    def __init__(self,id,name,email):
        self.id=id
        self.name = name
        self.email = email

    def display(self):
        print(self.id,self.name,self.email)

class student(clg):
    def __init__(self, id, name, email):
        super().__init__(id, name, email)

    def show(self):
        print(self.id,self.name,self.email)



c = clg(101,"jenil","j@gamil.com")
c.display()

s = student(102,"gajjar","gajjar90@gmail.com")
s.show()
s.display()


class student : 

    __name = "jenil"
    email = "jenil@gamil.com"

    def setdata(self,name):
        self.__name=name

    def show(self):
        print(self.__name,self.email)

s = student()
s.show()
s.setdata("gajjar")
s.show()


        







