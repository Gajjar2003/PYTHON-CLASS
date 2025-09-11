# Create a set

set = {"abc","deef",12,78,12,True}
print(set)

set = {"abc","deef",12,78,12,True}
print(type(set))


print("-------------------------------------------")

# set length

set = {"abc","deef",12,78,12,True}
print(len(set))

print("-------------------------------------------")

# set add and upadte

set = {"abc","deef",12,78,12,True}
set.add("jenil")
print(set) 

set.update({"gajjar"})
print(set) 


print("-------------------------------------------")

# set remove and pop and clear and discard and detele


set = {"abc","deef",12,78,12,True}
set.remove("abc")
print(set)

set.discard(12)
print(set)

set.pop()
print(set)

set.clear()
print(set)

del set


print("-------------------------------------------")

# set join 

# set union and update 

a = {1,2,3,4}
b = {5,6,7,8}

c = a.union(b)
print(c)

a.update(b)
print(a)

c = a|b
print(c)


#  set Intersection

a = {1,2,3,4}
b = {2,6,7,8}

c = a.intersection(b)
print(c)

c = a&b
print(c)

a.intersection_update(b)
print(a)


# Set different

a = {1,2,3,4}
b = {2,6,7,8}

c = a.difference(b)
print(c)

c = a-b
print(c)

a.difference_update(b)
print(a)


# set Symmetric Differences

a = {1,2,3,4}
b = {2,6,7,8}

c = a.symmetric_difference(b)
print(c)

c = a^b
print(c)

a.symmetric_difference_update(b)
print(a)


# set subset and superset and disjoint

a = {1,2,3,4}
b = {5,6,7,8}

print(b.issubset(a))
print(a.issuperset(b))
print(a.isdisjoint(b))