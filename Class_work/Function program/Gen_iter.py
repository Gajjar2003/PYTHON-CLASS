# l = [1,2,3,4,5,6,7,8,9]
# k = iter(l)
# print(next(k))
# print(next(k))
# print(next(k))

def squre(a):
    for i in range(1,a+a):
        yield i*i

a = iter(squre(5))
print(next(a))
print(next(a))
print(next(a))
print(next(a))