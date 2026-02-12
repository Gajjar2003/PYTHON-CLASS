# Function Practicals 

def name():
    print("Hello Well come to Python jenil")

name()


# ------------------------------------------


def add(a,b):
    return a+b

print(add(10,20))


# ------------------------------------------


def num(a,b,c):
  
    if (a > b and a > c ):
        print("first largest")
    elif(b > c  and b > a):
        print("second largest")
    else:
        print("thrid largest")

num(10,20,30)


# ------------------------------------------


def evenodd(a):
    if a %2 == 0:
        print("even")
    else:
        print("odd")

evenodd(11)

# ------------------------------------------

def square(a):
    return a*a

print(square(5))


# ------------------------------------------

def rev(s):
    return s[::-1]

print(rev("jenil"))

# ------------------------------------------

def palindrome(p):
    if p == p[::-1]:
        print("is palindrome ")
    else:
        print("palindrome not")

palindrome("jenil")

# ------------------------------------------

#  Practicals For-Loop

num = 10

for i in range(1,11):
    print( i ,"X",num ,"=",i*num)

# ------------------------------------------


fact = 10

for i in range(1,fact):
    fact = fact*i

    print(fact)

# ------------------------------------------

fibon = 10
pr = 0
pe = 1

for i in range(fibon):
    print(pr)
    temp = pr + pe
    pr = pe
    pe = temp

# ------------------------------------------

 
text = "jenil"

for ch in text:
    if ch in ["a","e","i","o","u"]:
        print(ch, "is vowel")
    else:
        print(ch, "is consonant")

# ------------------------------------------


num  = int(input("Enter your number is: "))

flage = 0

for i in range(2,num):
    if num %i==0:
        flage=1
        break
if flage==0:
    print("prime number")
else:
    print("Not a prime number")


# ------------------------------------------


num1 = input("Enter your number: ")

if num1 == num1[::-1]:
    print("Palindrome",num1)
else:
    print("Not Palindrome",num1)



num1 = 10

for i in range(1,11):
    if i == 5:
        break
    print(i)

print("--------------------------------")

for i in range(1,11):
    if i == 5:
        continue
    print(i)

