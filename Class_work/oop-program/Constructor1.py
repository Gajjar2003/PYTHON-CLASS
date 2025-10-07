class std :

    def __init__(self,*a):
        print("Hello",a)

    # def __init__(self,a,b):
    #     print("Hello",a,b)
    
    def show(self):
        print("Show calling...")

s = std(10)
s.show()