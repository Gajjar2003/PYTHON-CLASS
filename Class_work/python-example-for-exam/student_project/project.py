# 🏪 Student Record Management System
# 🎯 Project Overview

students = {}  

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    students[roll] = {"name": name, "marks": marks}
    print("✅ Student added successfully!\n")

def view_students():
    if not students:
        print("⚠️ No student records found!\n")
    else:
        print("\n--- Student Records ---")
        for roll, data in students.items():
            print(f"Roll: {roll}, Name: {data['name']}, Marks: {data['marks']}")
        print()

def search_student():
    roll = input("Enter Roll No to search: ")
    if roll in students:
        print(f"🎓 Found → Name: {students[roll]['name']}, Marks: {students[roll]['marks']}\n")
    else:
        print("❌ Student not found!\n")

def update_marks():
    roll = input("Enter Roll No to update: ")
    if roll in students:
        new_marks = int(input("Enter new marks: "))
        students[roll]["marks"] = new_marks
        print("✅ Marks updated!\n")
    else:
        print("❌ Student not found!\n")

def delete_student():
    roll = input("Enter Roll No to delete: ")
    if roll in students:
        del students[roll]
        print("🗑️ Student deleted!\n")
    else:
        print("❌ Student not found!\n")

def show_topper():
    if not students:
        print("⚠️ No student records!\n")
    else:
        topper = max(students.items(), key=lambda x: x[1]["marks"])
        print(f"🏆 Topper → Roll: {topper[0]}, Name: {topper[1]['name']}, Marks: {topper[1]['marks']}\n")

# Main Menu
while True:
    print("===== Student Record System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Show Topper")
    print("7. Exit")

    choice = input("Enter choice (1-7): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        show_topper()
    elif choice == "7":
        print("👋 Exiting... Bye!")
        break
    else:
        print("⚠️ Invalid choice, try again!\n")
