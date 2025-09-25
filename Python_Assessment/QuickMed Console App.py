# Module 6) Python - Fundamentals of python language
# Module 7) Python - Collections, functions and Modulesin Python
# QuickMed Console App
medicine_stock = {}

def add_medicine():
    print("*-*-*-*-*-*-*-*-*-* Add Medicine *-*-*-*-*-*-*-*-*-*-*-*-*")

    name = input("Enter medicine name: ").strip()
    price = float(input("Enter medicine price: "))
    stock = int(input("Enter medicine stock: "))

  
    medicine_stock[name] = [price, stock]

    print(f"✅ Medicine '{name}' added successfully!")

    add_choice = input("Do you want to add another medicine? (y/n): ").lower()
    if add_choice == "y":
        add_medicine()  
    else:
        print("Returning to main menu...")


def view_inventory():
    print("*-*-*-*-*-*-*-*-*-* View Inventory *-*-*-*-*-*-*-*-*-*-*-*-*")

    if not medicine_stock:  
        print("⚠️ Inventory is empty.")
        return

    for med, details in medicine_stock.items():
        print(f"{med} - Price: ₹{details[0]}, Stock: {details[1]}")








# while choice != "n":


#     print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
#     print("*            Quickmed pharmacy              *")
#     print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

#     print("Press 1 is Add medicine  ")
#     print("Press 2 is View inventory  ")
#     print("Press 3 is Update stock  ")
#     print("Press 4 is Sell medicine  ")
#     print("Press 5 is View sell report  ")
#     print("Press 6 is Exit ")


#     option = input("Please enter your choice is : ")




#     choice = input("Do you want to continue(y/n) : ")


