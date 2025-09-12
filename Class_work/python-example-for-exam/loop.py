# Write a program to print numbers from 1 to 10 using a for loop.

# for i in range(1,11):
#     print(i)


# Write a program to print numbers from 10 to 1 using a for loop.

# for i in range(10,0,-1):
#     print(i)



# Write a program to print the multiplication table of a given number.

# number = 12

# for i in range(1,number-1):
#     print(i , "X", number, "=",i*number)
# print()


# Write a program to find the sum of first N natural numbers using a for loop.

# num = int(input("Enter your number is: - "))
# total = 0

# for i in range(1,num+1):
#     total += i
# print("This sum of ",num,"And natural number ",total)


# Write a program to print even numbers between 1 and 20 using a while loop.

# num = 2

# while num != 20:
#     print(num)
#     num += 2


# Write a program to print odd numbers between 1 and 20 using a for loop.

# for num in range(1,21):
#     if num %2 == 0:
#         print(num)
    


# Write a program to reverse a number using a while loop.

# number = int(input("Enter your number is: "))

# rev = 0

# while number > 0:
#     digite = number%10
#     rev = rev * 10 + digite
#     number = number //10
# print("Reverse number is: ",rev)


# Write a program to calculate the factorial of a number using a for loop.
# num = 5

# for i in range(1,num):
#     num = num*i
# print("This nunber is factorial",num)

# Write a program to display the Fibonacci series up to N terms.

# f = 10 
# pr = 0 
# pe = 1

# for i in range(f):
#     temp = pr + pe
#     pr  = pe
#     pe = temp
#     print(pr)    



# Write a program to print the square of numbers from 1 to 10.

# for i in range(1,11):
#     print(i , "=" ,i*i)
#     i += 1
# print("Sum all element= ",i-1)


# Write a program to print all prime numbers between 1 and 50 using loops.


# for num in range(2, 51):  
#     flag = 0
#     for i in range(2, num):  
#         if num % i == 0:
#             flag = 1
#             break
#     if flag == 0:
#         print(num, end=" ")
