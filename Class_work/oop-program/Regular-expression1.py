import re

# check number expression 

print("******** Number exapression********")

num = input("Enter your number is : ")

n = re.match('[0-9]{10}$',num)

if n :
    print("Number is valid")
else:
    print("Number is invalid")



# check email expression 

print("******** Email exapression********")

email = input("Enter your email-id :  ")

e = re.match('[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email)

if e:
    print("Email is valid")
else:
    print("Email is Not valid")


# check password expression

print("******** Password exapression********")


import re

password = input("Enter your password: ")

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&]).{10,}$'

p = re.match(pattern, password)  
if p:
    print("✅ Password is correct")
else:
    print("❌ Password is incorrect")
