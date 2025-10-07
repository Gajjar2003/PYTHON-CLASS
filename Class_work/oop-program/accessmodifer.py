class demo :
    __name = "jenil"
    email = "jenil@gamil.com"

    def show(self):
        print(self.__name,self.email)

d =demo()
# print(dir(d))
# d._demo__name="abc"
d.show()