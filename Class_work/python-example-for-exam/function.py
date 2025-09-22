# Write a function to calculate the square of a number.

def squre(a):
    print(f"suqre of number is : {a*a}")


squre(5)

print("************************************************************************")

# write a function that takes two numbers as arguments and returns their sum.

def number(a,b):
    return a+b

k = number(10,20)
print(k)

print("************************************************************************")

# Write a function to find the factorial of a number.

def fact(a):
    result = 1
    for i in range(1,a+1):
        result *= i
    return result


num = 5 
print(f"factorial of",num,"is",fact(num))

print("************************************************************************")

# Write a function that checks if a number is even or odd.


def odd_even_check(num):
    if num %2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is Odd"
    

print(odd_even_check(1))
print(odd_even_check(13))   


print("************************************************************************")


# Write a function that returns the largest of three numbers.

def largest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
print(largest(120,45,755))