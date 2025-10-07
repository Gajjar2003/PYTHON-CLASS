class student : 

    __name = "jenil"
    email = "jenil@gamil.com"

    def setdata(self,name):
        self.__name=name

    def show(self):
        print(self.__name,self.email)

s = student()
s.show()
s.setdata("gajjar")
s.show()