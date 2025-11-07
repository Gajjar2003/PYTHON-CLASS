# Write a Python program to create a dictionary and display it.

d = {
    "name " :"jenil",
    "age" : 21,
    "email"  : "j@gamil.com"
}

print(d)

print("********************************************************")

# Write a Python program to access values using keys from a dictionary.

d = {
    "name " :"jenil",
    "age" : 21,
    "email"  : "j@gamil.com"
}
print(d.keys())


print("********************************************************")

# Write a Python program to update the value of a specific key in a dictionary.

d = {
    "name" :"jenil",
    "age" : 21,
    "email"  : "j@gamil.com"
}

d["name"] = "gajjar"
print(d)

print("********************************************************")

# Write a Python program to add a new key–value pair to a dictionary.


d.update({"suject" : "python"})
print(d)


print("********************************************************")

# Write a Python program to remove the last inserted item using popitem().

d.popitem()
print(d)

print("********************************************************")


# Write a Python program to check whether a key exists in a dictionary or not.

d = {
    "name" :"jenil",
    "age" : 21,
    "email"  : "j@gamil.com"
}

key = "age"

if key in d:
    print("exists is dic")
else:
    print("not exists is dic")

print("********************************************************")

# Write a Python program to get all keys of a dictionary.

# Write a Python program to get all values of a dictionary.

# Write a Python program to get all key–value pairs of a dictionary.


print(d.keys())
print(d.values())
print(d.items())

print("********************************************************")

# Write a Python program to find the length of a dictionary.

print(len(d))


print("********************************************************")

# Write a Python program to merge two dictionaries.

d = {
    "name" :"jenil",
    "age" : 21,
    "email"  : "j@gamil.com"
}

d1 = {
    "subject" : "python",
    "language" : "codding"
}

d3 = d | d1
print(d3)

print("********************************************************")

# Write a Python program to iterate through a dictionary (keys and values).

d = {
    "name": "jenil",
    "age": 21,
    "email": "j@gmail.com"
}

for key, value in d.items():
    print(key, ":", value)

print("********************************************************")

# Write a Python program to create a nested dictionary and access its elements

d = { 
    "jenil":{
    "age" : 21,
    "email" : "j@gamil.com"
},

    "om":{
        "age" : 22,
        "email" : "o@gamil.com"
    }

}

for i,j in d.items():
    print(i)
    for a,b in j.items():
        print(a,b)

print("********************************************************")

# Write a Python program to find the maximum and minimum values in a dictionary.

d = {
    "a": 10,
    "b": 25,
    "c": 5,
    "d": 40
}

maximum = max(d.values())
minimum = min(d.values())

print("Maximum value:", maximum)
print("Minimum value:", minimum)



print("********************************************************")

# Write a Python program to sort a dictionary by keys.

d = {
    "name": "jenil",
    "age": 21,
    "email": "j@gmail.com",
    "city": "Ahmedabad"
}


sorted_dict = dict(sorted(d.items()))

print(sorted_dict)

