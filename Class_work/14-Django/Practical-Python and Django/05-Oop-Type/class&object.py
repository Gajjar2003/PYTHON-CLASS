# Using oops -  simple class and object

#simple class & object and method use to construction

class Student:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email =email
    
    def show(self):
        print(f"student name is {self.name} and age is {self.age} and email is {self.email}")
        
s = Student("jenil",21,"jenil@gamil.com")
s.show()


class Car:
    def __init__(self,name,model,color,price):
        self.name=name
        self.model= model
        self.color = color
        self.price = price

    def display(self):
        print(f"{self.name}  model name {self.model} color is {self.color} and price is {self.price}")
        

c = Car("Od","A7","red",1585000)
c.display()