# Create a mini-project where students combine conditional statements, loops, and functions
# to create a basic Python application, such as a simple calculator or a grade management
# # system.

print("****************************************************")
print("*                                                  *")
print("*           Grade Management System                *")
print("*                                                  *")
print("****************************************************")

choice = "y"



while choice == "y":
    
    name = input("Enter your student name: ")
    marks = int(input("Enter your marks (0-100): "))



  
    if marks >= 90:
        grade = "A+ Grade"
    elif marks >= 80:
        grade = "A Grade"
    elif marks >= 70:
        grade = "B Grade"
    elif marks >= 60:
        grade = "C Grade"
    elif marks >= 50:
        grade = "D Grade"
    elif marks >= 40:
        grade = "E Grade"
    else:
        grade = "Fail!"


    
    choice = input("Do you want to continue? (y/n): ")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("Student name is",name)
print("student marks is",marks)
print("Student grade",grade)




