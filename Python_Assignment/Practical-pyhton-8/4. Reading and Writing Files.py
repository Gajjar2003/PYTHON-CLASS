# Write a Python program to read the contents of a file and print them on the console.

f = open("myfile.txt","r")
data = f.read()
print(data)
f.close()


# Write a Python program to write multiple strings into a file.

f = open("myfile.txt","w")
f.write("hello python")
f.write("\n hello java")
f.close()


# Python program to check the current position of the file cursor


file = open("myfile.txt", "r")

content = file.read(10)  
print("Content read:", content)
position = file.tell()
print("Current cursor position:", position)
file.close()
