# Write a program to print numbers from 1 to 10 using a for loop.

for i in range(1,11):
    print(i)


# Write a program to print numbers from 10 to 1 using a for loop.

for i in range(10,0,-1):
    print(i)



# Write a program to print the multiplication table of a given number.

number = 12

for i in range(1,number-1):
    print(i , "X", number, "=",i*number)
print()


# Write a program to find the sum of first N natural numbers using a for loop.

num = int(input("Enter your number is: - "))
total = 0

for i in range(1,num+1):
    total += i
print("This sum of ",num,"And natural number ",total)


# Write a program to print even numbers between 1 and 20 using a while loop.

num = 2

while num != 20:
    print(num)
    num += 2


# Write a program to print odd numbers between 1 and 20 using a for loop.

for num in range(1,21):
    if num %2 == 0:
        print(num)
    


