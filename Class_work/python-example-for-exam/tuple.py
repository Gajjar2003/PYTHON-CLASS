# Write a Python program to create a tuple and display it.

t  = (1,2,3,47,12.4,"jenil",1,True)
print(type(t))
print(t)
print("********************************************************")

# Write a Python program to access the first and last elements of a tuple.

t  = (1,2,3,47,12.4,"jenil",1,True)
print(t[1])
print(t[-1])

print("********************************************************")

# Write a Python program to find the length of a tuple.

t  = (1,2,3,47,12.4,"jenil",1,True)
print(len(t))

print("********************************************************")

# Write a Python program to convert a tuple into a list.

t  = (1,2,3,47,12.4,"jenil",1,True)
l  = list(t)
print(l)

print("********************************************************")

# Write a Python program to convert a list into a tuple.

l  = [3,4,1,8,7,9,5]

t = tuple(l)
print(type(t))
print(t)


print("********************************************************")

# Write a Python program to find the maximum and minimum elements of a tuple.

t  = (12,778,1845,15,16215,11,1,2544,333333)

maxmum = max(t)
minmum = min(t)

print(maxmum)
print(minmum)

print("********************************************************")

# Write a Python program to find the sum of all elements in a tuple.

t = (1,2,3,4,5,6,7,8,9,10,11,12)

total = sum(t)
print(total)

print("********************************************************")

# write a Python program to check whether an element exists in a tuple or not.

t = (1,2,3,4,5,6,7,8,9,10,11)
num = 13

if num in t:
    print(num,"exists")
else:
    print(num,"not exists")

print("********************************************************")

# Write a Python program to find the index of a particular element in a tuple.

t = (11,2,3,4,5,11,11,8,9,10,11)
num = 11

total = t.count(num)
print(total,"number is count")

print("********************************************************")

# Write a Python program to concatenate two tuples.

t = (1,2,3,4)
t1 = (5,6,7,8)

t2 = t + t1
print(t2)

print("********************************************************")


# Write a Python program to repeat a tuple multiple times.

t = (1,2,3,4)

repeat = t*2
print(repeat)

print("********************************************************")

# Write a Python program to slice a tuple (print specific elements using slicing).

t = (1,2,3,4,5,6,7,8,9,10)
print(t[0])
print(t[-1])
print(t[1:])
print(t[:9])
print(t[1:5])
print(t[2::])
print(t[::-2])
print(t[::-1])


print("********************************************************")

# Write a Python program to sort the elements of a tuple.

t = (1,2,3,4,5,6,7,8,9,10)

sort = sorted(t)
sort = sorted(t, reverse=True)

print(sort)

print("********************************************************")

# Write a Python program to create a nested tuple and access its elements.

t = ((1,2,3),(4,5,6),(7,8,9))

print(t[0][2])
print(t[1][2])
print(t[2][2])


print("********************************************************")

# Write a Python program to reverse a tuple.
t = (1,2,3,4,5,6,7,8,9,10)

print(t[::-1])

print("********************************************************")

# Write a Python program to check if two tuples are equal or not.


t = (1,2,3,4)
t1 = (1,2,3,4)

if t == t1:
    print("euqal")
else:
    print("not equal")

print("********************************************************")

# Write a Python program to unpack elements of a tuple into variables.

t = (1,2,3,4,5,6,7,8,9,10)

*a,b,c = t
print(a)
a,*b,c = t
print(b)
a,b,*c = t
print(c)

print("********************************************************")

# Write a Python program to convert a tuple of strings into a single string.

t = ("python","is","easy","to","language")

result = " ".join(t)
print(result)

print("********************************************************")

# Write a Python program to remove duplicate elements from a tuple.

t = (1,2,3,4,5,11,7,8,9,11,11,12,13,11,1,1,17,18,19,20)
num  = tuple(set(t))
print(num)

