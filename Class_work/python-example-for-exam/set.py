# Write a Python program to create a set and display it.

s = {1,2,3,4,5,6,"jenil","gajjar"}
print(s)
print(type(s))

print("*******************************************************************")

# Write a Python program to add a single element to a set.

s = {1,2,3,4}
s.add(5)
print(s)

# Write a Python program to add multiple elements to a set.

s = {1,2,3,4}
s.update([5,6,7,8])
print(s)


print("*******************************************************************")

# Write a Python program to remove an element from a set using remove().


s = {1,2,3,4}
s.remove(4)
print(s)

# Write a Python program to remove an element from a set using discard().

s = {1,2,3,4}
s.discard(4)
print(s)


# Write a Python program to pop a random element from a set.

s = {1,2,3,4}
s.pop()
print(s)

# Write a Python program to clear all elements of a set.

s = {1,2,3,4}
s.clear()
print(s)

print("*******************************************************************")

# Write a Python program to find the length of a set.

s = {1,2,3,4}
print(len(s))

print("*******************************************************************")

# Write a Python program to check if an element exists in a set or not.

s= {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
num = 12

if num in s:
    print(num,"exists")
else:
    print(num,"NOt exists")

print("*******************************************************************")

# Write a Python program to find the union of two sets.

s= {1,2,3,4}
s1 = {5,6,7,8}

set =s.union(s1)
print(set)

print("*******************************************************************")

# Write a Python program to find the intersection of two sets.

s= {1,2,3,4}
s1 = {3,4,7,8}

set = s.intersection(s1)
print(set)


# Write a Python program to find the difference of two sets.

s= {1,2,3,4}
s1 = {3,4,7,8}

set = s.difference(s1)
print(set)


# Write a Python program to find the symmetric difference of two sets.

s= {1,2,3,4}
s1 = {3,4,7,8}

set = s.symmetric_difference(s1)
print(set)

print("*******************************************************************")

# Write a Python program to check if a set is a subset of another set.

s= {1,2,3,4}
s1 = {1,2,3,4,5}

set = s.issubset(s1)
print(set)


# Write a Python program to check if a set is a superset of another set.

s= {1,2,3,4}
s1 = {1,2,3,4}

set  = s.issuperset(s1)
print(set)

print("*******************************************************************")

# Write a Python program to convert a list into a set.

# l = [1,2,3,4]

# s = set(l)
# print(s)


# Write a Python program to convert a set into a list.

s = {1,2,3,4}

l = list(s)
print(l)

print("*******************************************************************")

# Write a Python program to find the maximum and minimum values in a set.

s= {1,2445,141,771,685,27221,1855,8255,2}

maxmum = max(s)
minmum = min(s)
print(maxmum)
print(minmum)

print("*******************************************************************")

# Write a Python program to find the sum of all elements in a set.

s= {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
total = sum(s)
print(total)


print("*******************************************************************")

# Write a Python program to remove duplicate elements from a list using a set.


s= {11,2,3,4,5,6,7,8,9,11,11,11,11,14,15,16,11,18,11,20}
print(s)

