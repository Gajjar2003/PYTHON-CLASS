# Abstraction is unnecesary details from user method and class

class Car:
    def __init__(self,name,model,color,price):
        self.name=name
        self.model= model
        self.color = color
        self.price = price

    def display(self): # user se hidden he to ye method ko Abstraction 
        print(f"{self.name}  model name {self.model} color is {self.color} and price is {self.price}")
        

c = Car("Od","A7","red",1585000)
c.display()


class Student:
    def __init__(self,name,age,subjcet,total):
        self.name = name
        self.age = age
        self.subjcet = subjcet
        self.total = total
    
    def show(self): # user se hidden he to ye method ko Abstraction 
        print(f"Name is {self.name} age is {self.age} subjcet is {self.subjcet} and total is {self.total + 100}")
        # user ke  total me add 

s = Student("om",22,"HTML",450)
s.show()