# from multipledispatch import dispatch
# class Calc:

#     @dispatch(int, int)
#     def add(self,a,b):
#         print(a+b)

#     @dispatch(int,int,int)
#     def add(self,a,b,c):
#         print(a+b+c)

#     # def add(self,*a):
#     #     sum=0
#     #     for i in a:
#     #       sum+=i
#     #     print(sum)

# c = Calc()
# c.add(10,20)
# c.add(10,20,30)





class A:
    def display(self):
        print("A disp calling")

class B(A):
    def display(self):
        print("B disp calling")


b = B()
b.display()