class demo :
    id  = 10

    def display(self):
        print("display calling ..")

    @classmethod
    def simple(self):
        print("simple calling ...",self.id)

    @staticmethod
    def util(self):
        print("static calling")

    
d = demo()
d.display()
d.simple()

# demo.display()
demo.simple()
demo.util(10)