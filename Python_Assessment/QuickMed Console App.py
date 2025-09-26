# Module 6) Python - Fundamentals of python language
# Module 7) Python - Collections, functions and Modulesin Python
# QuickMed Console App
medicine_stock = {}
sales = []

import datetime

def add_medicine():
    print("*-*-*-*-*-*-*-*-*-* Add Medicine *-*-*-*-*-*-*-*-*-*-*-*-*")

    name = input("Enter medicine name: ")
    price_input = input("Enter medicine price: ")
    stock_input = input("Enter medicine stock: ")

    if price_input.replace('.', '', 1).isdigit() and stock_input.isdigit():
        price = float(price_input)
        stock = int(stock_input)
        medicine_stock[name] = [price, stock]
        print(f"✅ Medicine '{name}' added successfully!")
    else:
        print("❌ Invalid input! Price must be a number and stock must be an integer.")


def view_inventory():
    print("*-*-*-*-*-*-*-*-*-* View Inventory *-*-*-*-*-*-*-*-*-*-*-*-*")

    if not medicine_stock:
        print("⚠️ Inventory is empty.")
        return

    for med, details in medicine_stock.items():
        print(f"{med} - Price: ₹{details[0]}, Stock: {details[1]}")


def update_stock():
    print("*-*-*-*-*-*-*-*-*-* Update Stock *-*-*-*-*-*-*-*-*-*-*-*-*")
    name = input("Enter medicine name: ")

    if name not in medicine_stock:
        print("❌ Medicine not found in inventory.")
        return

    qty_input = input("Enter quantity to add: ")

    if qty_input.isdigit():
        qty = int(qty_input)
        if qty > 0:
            medicine_stock[name][1] += qty
            print(f"✅ Stock updated! {name} now has {medicine_stock[name][1]}")
        else:
            print("❌ Invalid quantity! Must be greater than 0.")
    else:
        print("❌ Invalid input! Please enter a number.")


def sell_medicine():
    print("*-*-*-*-*-*-*-*-*-* Sell Medicine *-*-*-*-*-*-*-*-*-*-*-*-*")
    customer = input("Enter customer name: ")
    name = input("Enter medicine name: ")

    if name not in medicine_stock:
        print("❌ Medicine not found in inventory.")
        return

    qty_input = input("Enter quantity purchased: ")

    if qty_input.isdigit():
        qty = int(qty_input)
    else:
        print("❌ Invalid quantity! Must be a number.")
        return

    price, stock = medicine_stock[name]
    if qty > stock:
        print(f"❌ Not enough stock! Available: {stock}")
        return

    medicine_stock[name][1] -= qty

    sale = {
        "customer": customer,
        "medicine": name,
        "quantity": qty,
        "total_price": price * qty,
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    sales.append(sale)

    print("\n✅ Sale Recorded Successfully!")
    print(f"Customer: {customer}")
    print(f"Medicine: {name}")
    print(f"Quantity: {qty}")
    print(f"Total Price: ₹{sale['total_price']}")
    print(f"Date: {sale['date']}")


def view_sales_report():
    print("\n=== Sales Report ===")
    if not sales:
        print("⚠️ No sales recorded yet.")
        return
    for s in sales:
        print(f"{s['date']} | Customer: {s['customer']} | Medicine: {s['medicine']} | "
              f"Qty: {s['quantity']} | Total: ₹{s['total_price']}")



while True:
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("*            QuickMed Pharmacy              *")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Press 1 → Add Medicine")
    print("Press 2 → View Inventory")
    print("Press 3 → Update Stock")
    print("Press 4 → Sell Medicine")
    print("Press 5 → View Sales Report")
    print("Press 6 → Exit")

    option = input("Please enter your choice: ")

    if option == "1":
        add_medicine()
    elif option == "2":
        view_inventory()
    elif option == "3":
        update_stock()
    elif option == "4":
        sell_medicine()
    elif option == "5":
        view_sales_report()
    elif option == "6":
        print("👋 Exiting... Thank you for using QuickMed!")
        break
    else:
        print("❌ Invalid choice. Please try again.")
