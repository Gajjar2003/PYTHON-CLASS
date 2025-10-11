class simaple:
    id = 101
    name = "jenil"

    def display(self):
        return f"my name is {self.name} and id is {self.id}"

class demo:
    s = simaple() 
    def show(self):
        return "show calling ..."

d = demo()
d.s.display()
print(d.s.display())