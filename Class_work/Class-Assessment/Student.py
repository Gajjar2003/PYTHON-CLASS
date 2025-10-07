# Student Record System

# Store student details (name, roll no, marks) in a dictionary.

# Add new students, view all students, search by roll number.


print(" -* Student Record System *- ")


student = {}

def add_student():
    add_choice = "y"
    while add_choice != "n":
        roll = int(input("Enter your roll number : "))
        name = input("Enter your name : ")
        marks = int(input("Enter your marks : "))

        student[roll] = {"name": name, "marks": marks}
        print("✅ Student added successfully!\n")

        add_choice = input("Do you want to continue (y/n): ")

def view_students():
    if not student:
        print("⚠ No student records found.\n")
    else:
        print("\n--- Student Records ---")
        for roll, details in student.items():
            print(f"Roll: {roll}, Name: {details['name']}, Marks: {details['marks']}")
        print()

def search_student():
    roll = int(input("Enter roll number to search: "))
    if roll in student:
        details = student[roll]
        print(f"✅ Found -> Roll: {roll}, Name: {details['name']}, Marks: {details['marks']}")
    else:
        print("⚠ Student not found.\n")

while True:
    print("\n1. Add new student")
    print("2. View all students")
    print("3. Search by roll number")
   

    option = int(input("Please enter your option (1-3): "))

    if option == 1:
        add_student()
    elif option == 2:
        view_students()
    elif option == 3:
        search_student()
    else:
        print("❌ Invalid option, try again.")

 


