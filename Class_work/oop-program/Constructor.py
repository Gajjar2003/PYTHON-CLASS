class student:

    collage = "svnit"

    def __init__(self,id,name,email):
        self.id = id
        self.name = name
        self.email = email

    def display(self):
        print("Student detils")
        print(self.id,self.name,self.email)    

    @classmethod
    def simple(self):
        print(self.collage)   

    @staticmethod
    def run():
        print("Run calling") 

student.run()

student.collage = "Abc"
student.simple()


s = student(1,"jenil","jenil@gamil.com")
s.display()

s1 = student(2,"nil","nil@gamil.com")
s1.display()