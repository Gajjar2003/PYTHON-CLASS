# file handling write mode 

f = open("test.txt","w")
f.write("Well come to be python")
f.close()


# file handling read mode

f = open("test.txt","r")
data = f.read()
print(data)

# file handling append mode

f = open("test.txt",'a')
f.write("\n Hello Java")
f.close()


# file handling readline mode 

f = open("test.txt",'r')
while True:
    data = f.readline()
    print(len(data))
    if 'Java' in data:
        print(data)
    if not data:
        break


# file handling readlines mode 

f = open("test.txt",'r')
data = f.readlines()
print(data)


# file handling with mode without file close mode 


with open("test.txt","r") as f:
    print(f.tell())
    f.seek(2)
    print(f.tell())
    data = f.read()
    print(f.tell())
    print(data)


#  file handling read + mode 

# with open('test1.txt','r+') as f:
#     f.write("something")
#     f.seek(0)
#     data = f.read()
#     print(data)



with open('test1.txt','w+') as f:
    f.write("something")
    f.seek(0)
    data = f.read()
    print(data)



#  file handling for image read for binary mode 

# with open("e:\photos\jenil photos\DROB6864.JPG","rb") as f:
#     data = f.read()
#     print(data)


