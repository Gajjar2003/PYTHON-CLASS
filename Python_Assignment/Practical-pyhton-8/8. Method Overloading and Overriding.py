# Write Python programs to demonstrate method overloading and method overriding


class MathOperation:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            print("Sum of three numbers:", a + b + c)
        elif a is not None and b is not None:
            print("Sum of two numbers:", a + b)
        else:
            print("Please provide at least two numbers.")


m = MathOperation()

# Example: Method Overriding

m.add(10, 20)        
m.add(5, 10, 15)     
m.add(10)            


class Animal:
    def sound(self):
        print("Animals make different sounds")

class Dog(Animal):
    def sound(self):
        print("Dog barks")


a = Animal()
d = Dog()

a.sound()   
d.sound()  
