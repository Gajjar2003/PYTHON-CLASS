# Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.).

# Single Inheritance Example


class Animal:
    def speak(self):
        print("Animal can make a sound.")


class Dog(Animal):
    def bark(self):
        print("Dog barks.")


d = Dog()
d.speak() 
d.bark()  


# Write a Python program to show multilevel inheritance.

class vehical:
    def vehical_type(self):
        print("this is a vehicals")

class car(vehical):
    def car_type(self):
        print("This is car")

class bilke(car):
    def bilke_type(self):
        print("This is bilke")


b = bilke()
b.vehical_type()
b.car_type()
b.bilke_type()


# Write a Python program to show multiple inheritance

class deposite:
    def dp(self):
        print("deposite it")

class balance:
    def bel(self):
        print("balance it")

class bank(deposite,balance):
    def bk(self):
        print("bank it")


b =bank()
b.dp()
b.bel()
b.bk()


# Write a Python program to show hierarchical inheritance

class Person:
    def greet(self):
        print("Hello!")


class Student(Person):
    def study(self):
        print("Student is studying.")


class Teacher(Person):
    def teach(self):
        print("Teacher is teaching.")


s1 = Student()
t1 = Teacher()

s1.greet()  
s1.study()  

t1.greet() 
t1.teach()



# Write a Python program to show hybrid inheritance


class A:
    def method_a(self):
        print("Method of A")


class B(A):
    def method_b(self):
        print("Method of B")


class C(A):
    def method_c(self):
        print("Method of C")


class D(B, C):
    def method_d(self):
        print("Method of D")


d = D()
d.method_a()  
d.method_b() 
d.method_c()  
d.method_d()  


# Write a Python program to demonstrate the use of super() in inheritance

# Python program to demonstrate the use of super() in inheritance


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  
        self.student_id = student_id

    def display(self):
        super().display()  
        print(f"Student ID: {self.student_id}")


s = Student("Jenil", 20, "S12345")
s.display()
