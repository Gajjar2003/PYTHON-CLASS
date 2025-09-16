def square(a):
    print(a*a)
    a+=1
    if a<20:
        square(a)

square(2)