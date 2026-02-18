# inheritance is  one class inher to another class (parent) to (child)


class Student:
    def __init__(self,roll,name,age,std,subject,email):
        self.roll = roll
        self.name = name
        self.age = age
        self.std = std
        self.subject = subject
        self.email = email

    def display(self):
        print(f" Roll number is {self.roll} Name is {self.name} age is {self.age} std to {self.std} subject is {self.subject} and email is {self.email}" )

class Techer(Student):
    def __init__(self, roll, name, age, std, subject, email,salary):
        super().__init__(roll, name, age, std, subject, email)
        self.salary = salary

    def show(self):
        super().display()   
        print(f"salary {self.salary} ")

s = Student(1,"jenil",22,12,"Python","jenil@gamil.com")
s.display()

t = Techer(101,"chitna",44,"MCA","Python","ch@gamil.com",25000)
t.show()

