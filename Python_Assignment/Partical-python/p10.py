#  Practical Example 1: Write a Python program to print each fruit in a list using a simple for loop. List1 = ['apple', 'banana', 'mango']

list = ["apple","banana","mango"]

for fruit in list:
    print(fruit)

print("********************************************************")    

# Practical Example 2: Write a Python program to find the length of each string in List1.

list = ["apple","banana","mango"]

for fruit in list:
    print(fruit, "= Length is: ", len(fruit))


print("********************************************************")   


# Practical Example 3: Write a Python program to find a specific string in the list using a simple for loop and if condition.

list = ["apple","banana","mango"]

item = input("Enter your fruit :- ")

for fruit in list:
    if fruit == item:
        print(item,"is found in the list !")
        break
    
else:
        print(item,"is not found the list ! ")


print("********************************************************")  


# Practical Example 4: Print this pattern using nested for loop:

# *
# * *
# * * *
# * * * *
# * * * * *

row = 10

for i in range(1,row,+1):
     for j in range(1,i+1):
          print("*",end=" ")
     print()        