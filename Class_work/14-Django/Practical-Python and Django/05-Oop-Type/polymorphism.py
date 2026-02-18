# polymorphism same name and same Operators name but diferent work for object 

class Student:
    def __init__(self,roll,name,age,std,subject,email):
        self.roll = roll
        self.name = name
        self.age = age
        self.std = std
        self.subject = subject
        self.email = email

    def show(self): # same method name but work is different
        print(f" Roll number is {self.roll} Name is {self.name} age is {self.age} std to {self.std} subject is {self.subject} and email is {self.email}" )

class Techer(Student):
    def __init__(self, roll, name, age, std, subject, email,salary):
        super().__init__(roll, name, age, std, subject, email)
        self.salary = salary

    def show(self): # same method name but work is different
       print(f" Roll number is {self.roll} Name is {self.name} age is {self.age} std to {self.std} subject is {self.subject} and email is {self.email} and salary is {self.salary}" )

s = Student(1,"jenil",22,12,"Python","jenil@gamil.com")
s.show()

t = Techer(101,"chitna",44,"MCA","Python","ch@gamil.com",25000)
t.show()
