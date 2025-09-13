#  Create Dictionaries

di = {
    "name" : "jenil",
    "age" : 21,
    "email" : "jenil@gamil.com"
}

print(di)

print("--------------------------------------")

# Dictionaries length

di = {
    "name" : "jenil",
    "age" : 21,
    "email" : "jenil@gamil.com"
}
print(len(di))
print(di['name'])
print(di.get("name"))

print("--------------------------------------")

# Dictionaries update

di = {
    "name" : "jenil",
    "age" : 21,
    "email" : "jenil@gamil.com"
}

di["name"]= "ravi"
print(di)
di.update({"subject": "python"})
print(di)
print(di["name"][0])

print("--------------------------------------")

#  Dictionaries key 

di = {
    "name" : "jenil",
    "age" : 21,
    "email" : "jenil@gamil.com"
}

print(di.values())
print(di.keys())
print(di.items())

print("--------------------------------------")

#  Dictionaries loop

di = {
    "name" : "jenil",
    "age" : 21,
    "email" : "jenil@gamil.com"
}

for i ,j in di.items():
    print(i,j)


di["name"]="jenil"
print(di)

di.update({"name":"vraj","phone":"123456789"})
print(di)

print("--------------------------------------")

#  Dictionaries pop and clear and detele

di = {
    "name" : "jenil",
    "age" : 21,
    "email" : "jenil@gamil.com"
}

di.pop("name")
print(di)
di.popitem()
print(di)
di.clear()
print(di)
del di

print("--------------------------------------")

# Nested Dictionaries

d2 = {

    "jenil":{
        "age": 21,
        "email" : "jenil@gamil.com"

    },

    "vraj":{
        "age" : 22,
        "email" : "vraj@gamil.com"


    }

}
for i , j in d2.items():
    print(i)
    for a,b in j.items():
        print(a,b)

print("--------------------------------------")

#  Dictionaries fromkeys

x = ('key1', 'key2', 'key3')
y = "Hello"
print(x,y)

thisdict = dict.fromkeys(x,y)
print(thisdict)

l = [1,2,3,4,5]


k = dict.fromkeys(l,a)
print(k)


