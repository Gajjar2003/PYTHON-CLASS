# Write a Python program to create a class and access its properties using an object.

class demo :
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"My name is {self.name} and age is {self.age}")


d = demo("jenil",22)
d.display()


# Write a Python program to demonstrate the use of local and global variables in a class.

# Global variable
school_name = "tops"


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("name", self.name)
        print("Age:", self.age)
        print("School:", school_name)  


student1 = Student("Jenil", 20)
student1.display()
