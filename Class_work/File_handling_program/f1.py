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