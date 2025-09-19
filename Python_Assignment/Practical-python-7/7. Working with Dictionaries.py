# Write a Python program to update a value in a dictionary


d = {
    "id" : 1,
    "name" : "jenil",
    "age" : 21,
    "coures" : "python",
    "city" : "surat",
    "email" : "jenil@gamil.com"
    
}

d["name"] = "meet"
d["age"] = 22

print(d)

print("***********************************************************************")


# Write a Python program to merge two lists into one dictionary using a loop.

keys = ["name","age","email"]
values = [ "jenil",21,"jenil@gamil.com"]

d = {}

for i in range(len(keys)):
    d  [keys[i]] = values[i]


print(d)

print("***********************************************************************")

# Write a Python program to update a value at a particular key in a dictionary. 

d = {
    "id" : 1,
    "name" : "jenil",
    "age" : 21,
    "coures" : "python",
    "city" : "surat",
    "email" : "jenil@gamil.com"
    
}

d["name"] = "meet"
d["age"] = 22

print(d)


print("***********************************************************************")


# Write a Python program to separate keys and values from a dictionary using keys() and values() methods


d = {
    "id" : 1,
    "name" : "jenil",
    "age" : 21,
    "coures" : "python",
    "city" : "surat",
    "email" : "jenil@gamil.com"
}

print(d.keys())
print(d.values())


print("***********************************************************************")

# Write a Python program to convert two lists into one dictionary using a for loop

keys = ["id", "name", "age", "course", "city"]
values = [1, "Jenil", 21, "Python", "Surat"]


d = {}


for i in range(len(keys)):
    d[keys[i]] = values[i]


print(d)


print("***********************************************************************")

#  Write a Python program to count how many times each character appears in a string

text = "programming in python"

ch_count = {}

for ch in text:
    if ch in ch_count:
        ch_count[ch] +=1
    else:
        ch_count[ch] = 1

for key,values in ch_count.items():
    print(f"{key}: {values}")