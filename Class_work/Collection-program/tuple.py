# Create a tuple

t = (10,545,78,12.4,"abc",True,12.4)
print(t)

t1 =tuple = (1,2,3,4,5,6,7,8,9,10.2,"xyz","xyz")
print(t1)


print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

# Tuple length

t = (10,545,78,12.4,"abc",True,12.4)
print(len(t))


print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

# Tuple index Position

t = (10,545,78,12.4,"abc",True,12.4)
print(t[1])
print(t[-1])
print(t[1:5])
print(t[1:])
print(t[:5])
print(t[::-1])

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

# Tuple convert list update

t = (10, 545, 78, 12.4, "abc", True, 12.4)

l = list(t)
l.append("jenil")
print(tuple(l))  
 
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

#  Unpack Tuples

t = ("apple","banana","mango","x","y","z","o")

(*a,b,c) = t

print(a)
print(b)
print(c)


print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

# Tupel for loop

t = ("apple","banana","mango","x","y","z","o")

for i in range(len(t)):
    print(t[i])


print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")    

# Tuple while loop

t = ("apple","banana","mango","x","y","z","o")
i = 0

while i < len(t):
    print(t[i])
    i = i + 1

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")        


# Tuple join

t1 = (1,2,3,4)
t2 = (5,6,7,8)

t3 = t1 + t2
print(t3)

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")   

# Tuple count

t = "jenil"
t1 = "gajjar"

t.count("j")
t1.index("j")

print(t)
print(t1)
