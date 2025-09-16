
a = 10

def test():
    global a
    a = 50
    print("test : ",a)


print(a)
test()
print(a)