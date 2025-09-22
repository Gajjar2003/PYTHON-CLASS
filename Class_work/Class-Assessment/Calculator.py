# Create a mini-project where students combine conditional statements, loops, and functions
# to create a basic Python application, such as a simple calculator or a grade management
# system.


print("****************************************************")
print("*                                                  *")
print("*         simple calculator system                 *")
print("*                                                  *")
print("****************************************************")

choice  = "y"

while choice != "n":

    print("Select operation : ")
    print("Press 1 is addition (+): ")
    print("Press 2 is Subtraction  (-): ")
    print("Press 3 is Multiplication  (*): ")
    print("Press 4 is Division  (/): ")

    option = input("Enter your choice is (1-4) : ")

    num1 = int(input("Please enter your first  number : "))
    num2 = int(input("Now secode number is : "))

    if option == "1":
        print(f"{num1} and {num2} addition is :  {num1+num2}")

    elif option == "2":
        print(f"{num1} and {num2} Subtraction is :  {num1-num2}")

    elif option == "3":
        print(f"{num1} and {num2} Multiplication is :  {num1*num2}")

    elif option == "4":
        print(f"{num1} and {num2} Division is :  {num1/num2}")
        
    else:
        print("Invalid choice ! ")
  
    
    choice = input("Do you want to continue? (y/n): ")





