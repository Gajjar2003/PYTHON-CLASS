class pen :
    price = 10
    name = "cello"
    color = "red"

    def display(self):
        print(self.price,self.name,self.color)

class notbook(pen):
    pages = 50 

    def show(self):
        self.price = 20
        print(self.price,self.name,self.color,self.pages)


p = pen()
p.display()

n = notbook()
n.show()



# ------------------------------- Constructor inheriance --------------------------------------------

class clg:
    
    def __init__(self,id,name,email):
        self.id=id
        self.name = name
        self.email = email

    def display(self):
        print(self.id,self.name,self.email)

class student(clg):
    def __init__(self, id, name, email):
        super().__init__(id, name, email)

    def show(self):
        print(self.id,self.name,self.email)



c = clg(101,"jenil","j@gamil.com")
c.display()

s = student(102,"gajjar","gajjar90@gmail.com")
s.show()
s.display()


# ----------------------------------------------------------------------------------------------------

class Animal : 

    def __init__(self,name):
        self.name = name

    def sleep():
        print("Animal is sleeping..")

    def eat():
        print("Animal is eating...")

class dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"The dog  {self.name} of breed is {self.breed} is barking .. ")

d = dog("Tommy","german shepherd")
d.bark()

# ----------------------------------------------------------------------------------------------------

class A:

    def __init__(self):
        print("A is calling...")

class B(A):

    def __init__(self):
        super().__init__()
        print("B calling ...")

b = B()

