print("Program started")
try :
    a = 10
    b  =a/2
    print(b)
except Exception as e:
    print(e)
else:
    print("everything is oky")
finally:
    print("ALways executable")

print("Program ended")



f = None
try:
    f = open("test.txt", 'r')
    data = f.read()
    print(data)
except Exception as e:
    print(e)
finally:
    if f is not None:
        f.close()



def test():
    try :
        a = int(input("Enter number : "))
        return 1
    except Exception as e:
        return 0
    finally :
        print("Program exected...")

a = test()
print(a)