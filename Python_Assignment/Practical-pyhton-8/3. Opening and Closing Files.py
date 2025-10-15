# Write a Python program to open a file in write mode, write some text, and then close it

f = open("file.txt","w")
f.write("hello python")
f.close()



# Write a Python program to create a file and write a string into it.


file = open("myfile.txt", "w")
file.write("Hello, this is a sample text written to a file!")
file.close()
print("written successfully.")
