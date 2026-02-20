# File handling means reading and writing data in a file using Python.

# File writing mode

# f = open("demo.txt", "w")
# f.write("Hello Jenil")
# f.close()

# File reading mode

# f = open("demo.txt","r")
# data = f.read()
# print(data)
# f.close()

# File append mode

# f = open("demo.txt","a")
# f.write("\nWell come to be python ")
# f.write("\nPython is simple English")
# f.close()

# f = open("demo.txt","r")
# data = f.read()
# print(data)
# f.close()


# ---------------------------------------------------------------

f = open("test.txt","w")
f.write("Well come to file handing topices ...")
f.close()

f = open("test.txt","r")
data = f.read()
print(data)
f.close()

f = open("test.txt","a")
f.write("\nFile handing to read,write and appand mode to be python topices...")
f.close()


# read , readline , readlines 

f = open("test.txt","r")
data = f.read()           # read mode is single file read
print(data)
f.close()

f = open("test.txt","r")
data = f.readline()         # readline mode is one by one line read    
print(data)
f.close()

f = open("test.txt","r")    # readlines mode is all line read and return to be list 
data = f.readlines()
print(data)
f.close()


# seek and tell method 

f = open("show.txt","r")

print(f.tell())   # cursor current position batata hai
f.read(5)
print(f.tell())   


f.seek(0)         # Cursor wapas start me le gaye
print(f.tell()) 
print(f.read(10))  
