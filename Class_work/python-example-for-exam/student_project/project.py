# 🏪 Student Record Management System
# 🎯 Project Overview
student_recode = {}


student_recode = {}

def add_student():
    print("\n--- Add Student ---")
    roll = int(input("Enter your roll number: "))
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    subject = input("Enter subject: ")

    student_recode[roll] = {"name": name, "marks": marks, "subject": subject}
    print("✅ Student added successfully!\n")

def view_students():
    if not student_recode:
        print("⚠️ No student records found!\n")
    else:
        print("\n--- Student Records ---")
        for roll, data in student_recode.items():
            print(f"Roll: {roll}, Name: {data['name']}, Marks: {data['marks']}, Subject: {data['subject']}")
        print()

def search_student():
    roll = input("Enter Roll No to search: ")
    if roll in student_recode:
        print(f"🎓 Found → Name: {student_recode[roll]['name']}, Marks: {student_recode[roll]['marks']}\n")
    else:
        print("❌ Student not found!\n")






add_student()

search_student()












# print("/*/*/*/*/*/*/*/*/*/* Student Record Management System */*/*/*/*/*/*/*/*/*/*/*/")


# print("Press 1 is add student  ")
# print("Press 2 is view all student  ")
# print("Press 3 is search student by Roll nomber ")
# print("Press 4 is update marks  ")
# print("Press 5 is delete student ")
# print("Press 6 is student topper ")

