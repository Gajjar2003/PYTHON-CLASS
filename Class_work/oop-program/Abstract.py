from abc import ABC,abstractmethod

class demo(ABC):

    @abstractmethod
    def test(self):
        pass

class demoimp(demo):

    def test(self):
        print("testing...")


# d = demo()
# d.test()


d =demoimp()
d.test()