# Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).
# Simple Calculator with Exception Handling

# try:
   
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))


#     operation = input("Enter operation (+, -, *, /): ")

  
#     if operation == '+':
#         result = num1 + num2
#     elif operation == '-':
#         result = num1 - num2
#     elif operation == '*':
#         result = num1 * num2
#     elif operation == '/':
#         result = num1 / num2
#     else:
#         raise ValueError("Invalid operation")  
#     print(f"Result: {result}")


# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed!")


# except ValueError as ve:
#     print("Error:", ve)


# except Exception as e:
#     print("An unexpected error occurred:", e)


# # Write a Python program to demonstrate handling multiple exceptions.



# try:
 
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))

  
#     result = num1 / num2

  
#     my_list = [1, 2, 3]
#     print("Accessing invalid index:", my_list[5])

# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed!")

# except ValueError:
#     print("Error: Invalid input! Please enter a number.")

# except IndexError:
#     print("Error: List index out of range!")

# except Exception as e:
#     print("An unexpected error occurred:", e)

# else:
#     print("Division Result:", result)

# finally:
#     print("Execution completed.")



# Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).

# try:
    
#     filename = input("Enter the filename to read: ")
#     file = open(filename, "r") 
#     content = file.read()
#     print("File contents:\n", content)
#     file.close()


#     num1 = int(input("Enter numerator: "))
#     num2 = int(input("Enter denominator: "))
#     result = num1 / num2  
#     print("Division Result:", result)

# except FileNotFoundError:
#     print("Error: File not found!")

# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed!")

# except ValueError:
#     print("Error: Invalid input! Please enter numeric values.")

# except Exception as e:
#     print("An unexpected error occurred:", e)

# finally:
#     print("Program execution completed.")


# Write a Python program to handle file exceptions and use the finally block for closing the file



# filename = input("Enter the filename to read: ")

# try:
   
#     file = open(filename, "r")
#     content = file.read()
#     print("File contents:\n", content)

# except FileNotFoundError:
#     print("Error: The file does not exist!")

# except IOError:
#     print("Error: An I/O error occurred while handling the file!")

# finally:
   
#     try:
#         file.close()
#         print("File closed successfully.")
#     except NameError:
       
#         print("File was not opened, so no need to close.")


# Write a Python program to print custom exceptions.

class MyCustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def check_value(x):
    if x < 0:
        raise MyCustomError("Error: Negative values are not allowed!")
    elif x == 0:
        raise MyCustomError("Error: Zero is not a valid input!")
    else:
        print(f"Value {x} is valid.")


try:
    num = int(input("Enter a number: "))
    check_value(num)

except MyCustomError as e:
    print("Custom Exception Caught:", e)

except ValueError:
    print("Error: Please enter a valid integer.")
