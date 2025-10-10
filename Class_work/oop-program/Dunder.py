
class demo:

    id = 101
    name = "jenil"

    def __str__(self):
        return f"my name is {self.name} and id is {self.id}"
    
d =demo()
print(d)



class calc:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self,object):
        return self.a+object.a,self.b+object.b
    


    
c = calc(10,20)
c1  =  calc(10,20)

k = c + c1
print(k)


class multiple:
    def __init__(self,a,b):
        self.a = a
        self.b = b 

    def __mul__(self,mu):
        return self.a*mu.a,self.b*mu.b




m = multiple(5,10)
m1 = multiple(25,11)

n = m * m1
print(n)

        


