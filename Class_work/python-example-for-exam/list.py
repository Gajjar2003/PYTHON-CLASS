# Write a Python program to create a list of 5 numbers and display it.

l = ["jenil",1,"gajjar",2,15.4,True,14]

print(l[5])

print("**************************************************")

# Write a Python program to access the first and last elements of a list.

l =  [1,14,77,48,54,587,877,5444,2121]

print(l[1])
print(l[-1])


print("**************************************************")

# Write a Python program to update the third element of a list.

l = ["jenil",1,"gajjar",2,15.4,True,14]
l[3] = "ravi"
print(l)

print("**************************************************")

# Write a Python program to append a new element to a list.

l = ["jenil",1,"gajjar",2,15.4,True,14]
l.append("ramchandar")
print(l)

print("**************************************************")

# Write a Python program to insert an element at the second position in a list.

l = ["jenil",1,"gajjar",2,15.4,True,14]
l.insert(2,"vraj")
print(l)

print("**************************************************")

# Write a Python program to remove an element from a list using remove().

l = ["jenil",1,"gajjar",2,15.4,True,14]
l.remove("jenil")
print(l)

print("**************************************************")

# Write a Python program to delete an element from a list using del.

# l = ["jenil",1,"gajjar",2,15.4,True,14]
# del l
# print(l)

print("**************************************************")

# Write a Python program to sort a list in ascending order.

l1 = [14,1,547,7,8872,77,5485,5,7444,11]
l1 .sort()
print(l1)

print("**************************************************")

# Write a Python program to sort a list in descending order.

l1 = [14,1,547,7,8872,77,5485,5,7444,11]
l1 .sort(reverse=True)
print(l1)

print("**************************************************")

# Write a Python program to reverse a list.

l1 = [14,1,547,7,8872,77,5485,5,7444,11]
l1 .reverse()
print(l1)

print("**************************************************")

# Write a Python program to find the maximum and minimum elements of a list.

l1 = [14,1,547,7,8872,77,5485,5,7444,11]

maximun = max(l1)
mininum = min(l1)
print(maximun)
print(mininum)

print("**************************************************")

# Write a Python program to find the sum of all elements in a list.

l1 = [14,1,547,7,8872,77,5485,5,7444,11]
total =sum(l1)
print(total)

print("**************************************************")

# Write a Python program to count the number of times a particular element appears in a list.

l1 = [14,11,547,11,8872,11,5485,5,7444,11]
element =11

count = l1.count(element)
print(count)

print("**************************************************")

# Write a Python program to check whether an element exists in a list or not.

l1 = [14,11,547,11,8872,11,5485,5,7444,11]
num = 11

if num in l1:
    print(num,"exists in a list")
else:
    print(num,"not exists in a list ")

print("**************************************************")


# Write a Python program to create a nested list and access its elements.

l1  = [[1,2,3],[4,5,6],[7,8,9]]

print(l1[0][2])
print(l1[1][2])
print(l1[2][2])

print("**************************************************")

# Write a Python program to print only even numbers from a list.

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for num in l:
    if num %2 == 0 :
        print(num)
    

print("**************************************************")

# Write a Python program to print only odd numbers from a list.

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for num in l:
    if num %2 != 0 :
        print(num)


print("**************************************************")

# Write a Python program to remove duplicate elements from a list.

l = [1,2,3,4,5,11,7,8,9,11,11,12,13,11,1,1,17,18,19,20]

num = list(set(l))
print(num)

print("**************************************************")

# Write a Python program to find the length of a list without using len().

l = [1,2,3,4,5,11,7,8,9,11,11,12,13,11,1,1,17,18,19,20]
print(len(l))


print("**************************************************")

# Write a Python program to copy all elements of one list into another list.

l = [1,2,3,4,5,11,7,8,9,11,11,12,13,11,1,1,17,18,19,20]

l = l1.copy()
print(l)
