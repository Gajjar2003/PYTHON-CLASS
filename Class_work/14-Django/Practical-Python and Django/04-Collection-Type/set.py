# set all method in Practicals (set is  unordered and mutable and  no duplicate allow and writting to {} )

s = {1,2,3,4,5,6,7,8,9}
print(len(s))
print(type(s))
print(s)


s = {1,2,3,4}
s.add(5)
print(s)

s = {1,2}
s2 = {3,4}
s.update(s2)
print(s)

s = {"jenil"}     # set1 and set2 ko join karta he 
s2 = {"gajjar"}    # symbol |
s3 = s.union(s2)
print(s3)


s = {1,2,3,4,5}  # set1 and set2 me same value output degaa
s1 = {2,7,8,9,10}   # symbol &

s2 = s.intersection(s1)
print(s2)


s = {1,2,3,4,5,6}    # set1 and set2 me same value he vo remove kare ga and baki value degaa
s1 = {2,7,8,9,10,11}    # symbol ^

s2 = s.symmetric_difference(s1)
print(s2)

s = {1,2,3}
s1 = {1,2,3}    # set1 and set2 dono set same he to true degaa nahi to false 

s2 = s.issubset(s1)
print(s2)


s = {1,2,3}         # set1 ke andar set2 ke saare element he to True and false
s1 = {4,5,6}

s2 = s.issuperset(s1)
print(s2)

s = {1,2}  # set1 and set2 ke andar value same nahi he to True and false 
s1 = {3,4}

s2 = s.isdisjoint(s1)
print(s2)