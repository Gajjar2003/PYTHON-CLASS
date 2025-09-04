# Create a list 

l = [12,45,78,"jenil","gajjar", 45.78]
print(l)
l1 =list = [10,1,3,47,454]
print(l1)

print("-------------------------------------------------------------")

# list length

l = [12,45,78,"jenil","gajjar", 45.78]
print(len(l))


print("-------------------------------------------------------------")

# List index Position

Name = ["jenil","aniket","yug","meet","darshan"]
print(Name[1])
print(Name[-1])
print(Name[1:3])
print(Name[::-1])

print("-------------------------------------------------------------")

# list add 

Name[1] = "Dhruvin"
print(Name)

Name[1:3] = "ravi"
print(Name)

Name.insert(1,"gajjar")
print(Name)

Name.append("vraj")
print(Name)

N = ["a","b","hello"]
Name.extend(N)
print(Name)


print("-------------------------------------------------------------")

# List remove

Name.remove("hello")
print(Name)

Name.pop()
print(Name)

Name.pop(1)
print(Name)

# Name.clear()
# print(Name)

# del Name


print("-------------------------------------------------------------")
print("-------------------------------------------------------------")

# List  For Loop

for i in Name:
    print(Name)


for i in range(len(Name)):
    print(Name[i])

print("-------------------------------------------------------------")

# List while loop

i = 0

while i < len(Name):
    print(Name[i])
    i += 1


print("-------------------------------------------------------------")


k = []

for i in Name:
    if "e" in i:
        k.append(i)
print(k)

print("-------------------------------------------------------------")


# List Comprehension

k = [ i for i in Name if "e" in i]
print(k)

k = [i for i in Name if i.startswith('d')]
print(k)

k = ["j" for i in Name]
print(k)


print("-------------------------------------------------------------")

# List Sort

Name . sort()
print(Name)

Name . sort(reverse=True)
print(Name)

Name.reverse()
print(Name)


k = sorted(Name)
print(Name)

print("-------------------------------------------------------------")


# List Copy

k = Name.copy()
print(k)

k = Name[:]
print(k)

k = Name
print(k)

print("-------------------------------------------------------------")

# List Join

a = [1,2,3,4]
b = [5,6,7,8]

c = a + b
print(c)

a.extend(b)
print(a)

print("-------------------------------------------------------------")

# List count

print(a.index(2))

print(a.index(2))