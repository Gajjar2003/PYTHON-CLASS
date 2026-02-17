# dic all method in Practicals (dic is  ordered and  mutable and  no duplicate allow and writting to {} and store to key(unique) and value(any data-type))


d = {
    "name" : "jenil",
    "age" : 21
}

print(d)
print(type(d))
print(len(d))

d = {
    1 : "jenil",
    2:  21
}
print(d)


d = {
    1.5 : "jenil",
    2.8:  21
}
print(d)



d = {
    True : "jenil",
    False:  21
}
print(d)



d = {
   (1,2) : "jenil",
    (3,4):  21
}
print(d)

d = {
    "name" : "jenil",
    "age" : 21
}

print(d.keys())
print(d.values())
print(d.items())


d = {
    "name" : "jenil",
    "age" : 21
}

d["name"]= "om"
print(d)

d.update({"name":"Prem"})
print(d)

d.update({"email" : "prem@gamil.com"})
print(d)


d = {
    "name" : "om",
    "age" : 21,
    "email" : "om@gamil.com"

}

for i in d.items() :
  print(i)


d = {
    
    "jenil": {

        "name" : "gajjar",
        "age"  : 21
       },

    "yug" : {
      
        "name" : "patel",
        "age" : 22
    }
    
}
print(d["yug"]["age"])

d = {
  "name" : "od",
  "model" : "A7"
}
d1 = d.get("model")
print(d1)