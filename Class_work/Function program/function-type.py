#  Create function

def hello():
    print("well come to python language")


hello()
hello()

print("***************************************************")

# Function single arguments

def squre(a):
    print(a*a)

squre(5)

# Function multiple arguments

def add(a,b):
    print(a+b)

add(20,30)

print("***************************************************")

# Return Values

def add(a,b):
    return a+b

def squre(a):
    return a*a

k = add(10,20)
j = squre(k)

print(j)


print("***************************************************")

# Default Parameter Value

def preson(id=0,name="jenil",email="xyz@gmail.com"):
    print(id,name,email)

preson("ravi",email="ravi@gamil.com")

def person(**a):
    print(a)

person(name="dhurvin",email="dv@gmail.com")

print("***************************************************")

# Arbitrary Arguments

def add(*a):
    print(a)

a = add(10,20,30,40,50,60,70,80,90)

a = lambda a,b:a+b
b = lambda a: a*a

print(a(10,20))
print(b(25))

