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


print("************************************************************************")

# Write a function to check if a string is a palindrome.

def is_palindrome_number(number):
    temp = number
    rev = 0

    while number != 0:
        rem = number % 10
        rev = rev * 10 + rem
        number //= 10

    if rev == temp:
        print(temp, "is a Palindrome number")
    else:
        print(temp, "is Not a Palindrome number")


is_palindrome_number(121)
is_palindrome_number(123)


print("************************************************************************")

# Write a function to find the Fibonacci sequence up to n terms.

def fibobaccci(a):
    temp = number
    pe = 0 
    pr = 1

    for i in range(a):
        temp= pe+pr
        pe = pr
        pr =temp

        print(temp,"fibonacci ")

fibobaccci(10)



print("************************************************************************")

# Write a function that accepts a list of numbers and returns the maximum element.

def find_max(nums):
    return max(nums)


print(find_max([12, 45, 2, 89, 34]))

print("************************************************************************")

# Write a function to calculate the area and perimeter of a rectangle.

def rectangle_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


a, p = rectangle_area_perimeter(100, 5)
print("Area:", a)
print("Perimeter:", p)


print("************************************************************************")

# Write a function that takes a list and returns a new list with only unique elements.
def unique(lst):
    return list(set(lst))

print(unique([1, 45, "%", "@", 45]))
