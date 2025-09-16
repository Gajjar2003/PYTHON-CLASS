# write a program to  list in element for squer without using map function

l = [10,20,30,40,50,60,70,80,90,100]

def squre(a):
    return a*a

s = []
for i in l:
    k = squre(i)
    s.append(k)
print(s)

#  USing map function 

s = map(squre,l)
s = map(lambda a:a*a,l)
print(list(s))

print("*******************************************************************************************")

# write a prgram to odd and even number without using filter function

l = [1,2,3,4,5,6,7,8]

def oddnumber(a):
    if a%2 != 0:
        return True
    else:
        return False
    
s = []

for i in l:
    k = oddnumber(i)
    if k :
        s.append(i)
print(s)

#  Using filter function

s = filter(oddnumber,l)
s = filter(lambda a : a%2!=0,l)
print(list(s))



print("*******************************************************************************************")

# write a program to maxmum value find to list using without reduce function

from functools import reduce

l = [1,2,3,45,6,7,87,92,2,92]

def max(a,b):
    if a > b:
        return a
    else:
        return b
    

k = reduce(max,l)
k = reduce(lambda a,b:a+b,l)
k = reduce(lambda a,b: a if a>b else b,l)

print(k)