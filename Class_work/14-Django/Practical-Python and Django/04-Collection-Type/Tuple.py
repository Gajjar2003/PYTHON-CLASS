# Tuple all method in Practicals (Tuple is  Ordered and unmutable and duplicate all and writting to () )

t = (1,2,3,4,5)
print(t)
print(type(t))
print(len(t))

t = (1,2,3,4)
print(t[2])

t = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(t[4::])
print(t[2::4])
print(t[::-1])

t = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
if "apple" in t:
    print("is exists")
else:
    print("Not exists")


t = (1,2,3,4)   # Original tuple

l = list(t)    # Tuple → List
l.append(5)    # List me value add ki

t = tuple(l)   # List → Tuple
print(t)


t = (1,2,3,4) # same to same process to pop and clear

l = list(t)
l.remove(4)

t = tuple(l)
print(t)

