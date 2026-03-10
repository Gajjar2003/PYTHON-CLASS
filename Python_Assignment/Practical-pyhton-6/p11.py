# Write a generator function that generates the first 10 even numbers


def even_numbers():
    num = 2
    count = 0
    while count < 10:
        yield num
        num += 2
        count += 1


for n in even_numbers():
    print(n)

print("*******************************************************************")

# Write a Python program that uses a custom iterator to iterate over a list of integers.


l = [10,12,13,14,15,16,17,18,19]

k = iter(l)
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))