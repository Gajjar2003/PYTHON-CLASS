# Create a mini-project where students combine conditional statements, loops, and functions
# to create a basic Python application, such as a simple calculator or a grade management
# system.


print("****************************************************")
print("*                                                  *")
print("*           Grade Management System                *")
print("*                                                  *")
print("****************************************************")

students = []
choice  = "y"
while choice != "n":


    name =   input ("Enter your student name is : ")
    marks = int(input("Please enter your marks : "))

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    elif marks >= 40:
        grade = "Pass"
    else:
        grade = "Fail"

    print(f"You are {grade} Grade")

    students.append({"name": name, "marks": marks, "grade": grade})

    choice = input("Do you want continue ? (y/n): ")


print("*******Student Marks Sheet *******")
for s in students:
    print(f"Student Name : {s['name']}, Marks : {s['marks']}, Grade : {s['grade']}")








