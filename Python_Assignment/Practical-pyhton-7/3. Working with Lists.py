# Write a Python program to iterate over a list using a for loop.

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for i in l:
    print(i)

print("*******************************************************************")

# Write a Python program to sort a list using both sort() and sorted().

l = [31,32,53,46,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

l.sort()
print(l)

l.sort(reverse=True)
print(l)


l = [4,774,88,477,82,1,54]

k = sorted(l)
print(k)

k = sorted(l,reverse=True)
print(k)


print("*******************************************************************")


# Write a Python program to iterate through a list and print each element

list = ["apple", "banana","mango"]

for i in list:
    print(i)

print("*******************************************************************")


# Write a Python program to insert elements into an empty list using a for loop and append()

list = ["apple", "banana", "mango"]  
s = []

for i in list:       
    s.append(i)       

print(s)

        
