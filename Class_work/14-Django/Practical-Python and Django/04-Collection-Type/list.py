# List all method in Practicals (list is  Ordered and mutable and duplicate allow  and writting to [])

l = [1,2,3,4,5,6]
print(type(l))

l = [1,2,3,4,5,6]
print(len(l))

l = [1,2,3,4,5,6]
print(l)

l = [11,12,13,14,15,16]
print(l.index(13))

l = [1,2,3,4,5,6]
l.append(7)
print(l)

l = [1,2,3,4,5,6]
l.insert(0,100)
print(l)


l = [1,2]
l.extend([3,4])
print(l)


l = [1,2,3,4,5]
l.pop()
print(l)

l = [1,2,3,4,5]
l.remove(2)
print(l)

l = [1,2,3,4,5]
l.clear()
print(l)

l = [1,2,2,2]
l.count(2)
print(l)

l = [11,2,23,84]
l.sort()
print(l)

l = [1,2,3]
l1 = l.copy()
print(l1)

l = [1,2,3,4]
t = tuple(l)
print(t)
print(type(t))

l = [1,2,3,4,5,6,7,8,9,10]
l.reverse()
print(l)

l = [1,2,3,4,5,6]
l[1]= 200
print(l)