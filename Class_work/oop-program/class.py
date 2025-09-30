class demo:
    price  = 10
    company = "cello"
    color = "blue"

    def write(self):
        print("write calling...")
        print(self.price,self.company,self.color)

d = demo()
d.write()

d1 = demo()
d1.price = 1250
d1.write()