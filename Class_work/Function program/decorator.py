def beforeTest(test):
    def wrapper():
        print("call before test")
        test()
    return wrapper


@beforeTest
def test():
    print("Test calling...")

@beforeTest
def demo():
    print("Demo calling")


test()
demo()



def add(calc):
    def wrapper(*a):
        print(a[0]+a[1])
        calc(*a)
    return wrapper

def mul(calc):
    def wrapper(*a):
        print(a[0]*a[1])
        calc(*a)
    return wrapper

@mul
@add
def calc(a,b):
    print("Calc operation")


calc(10,20)