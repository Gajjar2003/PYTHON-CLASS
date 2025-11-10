from tkinter import *
import mysql.connector as sql

root = Tk()
root.geometry("500x500")

def insert():
    name = e1.get()
    email = e2.get()
    phone = e3.get()

    con = sql.connect(
        host="localhost",
        user="root",
        password="Admin@123",
        port=3306,
        database="pythonsql"
    )
    cursor = con.cursor()
   
    query = "INSERT INTO emp (name, email, phone) VALUES (%s, %s, %s)"
    values = (name, email, phone)
    cursor.execute(query, values)
    con.commit()
    print("Data inserted")
    con.close()

l1 = Label(root, text="Name").place(x=200, y=100)
l2 = Label(root, text="Email").place(x=200, y=150)
l3 = Label(root, text="Phone").place(x=200, y=200)

e1 = Entry(root)
e1.place(x=300, y=100)

e2 = Entry(root)
e2.place(x=300, y=150)

e3 = Entry(root)
e3.place(x=300, y=200)

b1 = Button(root, text="Submit", width=15, command=insert)
b1.place(x=300, y=230)

root.mainloop()
