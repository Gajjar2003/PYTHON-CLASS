# Create a mini-project where students combine conditional statements, loops, and functions
# to create a basic Python application, such as a simple calculator or a grade management
# system.


print("****************************************************")
print("*                                                  *")
print("*           Grade Management System                *")
print("*                                                  *")
print("****************************************************")


def calculate_grade(marks):
    if marks >= 90:
        return "A+ Grade"
    elif marks >= 80:
        return "A Grade"
    elif marks >= 70:
        return "B Grade"
    elif marks >= 60:
        return "C Grade"
    elif marks >= 50:
        return "D Grade"
    elif marks >= 40:
        return "E Grade"
    else:
        return "Fail!"


students = []

choice = "y"

while choice.lower() == "y":
    name = input("Enter your student name: ")
    marks = int(input("Enter your marks (0-100): "))
    
    grade = calculate_grade(marks)
    
 
    students.append({"name": name, "marks": marks, "grade": grade})
    
    choice = input("Do you want to continue? (y/n): ")

print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("All Student Records:")
print("Name\tMarks\tGrade")
for student in students:
    print(f"{student['name']}\t{student['marks']}\t{student['grade']}")



