from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector as sql

con = sql.connect(
    host="localhost",
    user="root",
    password="Admin@123",
    port=3306,
    database="pythonsql"
)

root = Tk()
root.geometry("800x500")


def show():
    cursor = con.cursor()
    cursor.execute("SELECT * FROM emp")
    data = cursor.fetchall()

  
    for i in table.get_children():
        table.delete(i)

    for i, (id, name, password, email) in enumerate(data, start=1):
        table.insert("", END, values=(id, name, password, email))


def add_data():
    name = e1.get()
    password = e2.get()
    email = e3.get()

    cursor = con.cursor()
    qry = "INSERT INTO emp(id, name, password, email) VALUES(%s, %s, %s, %s)"
    val = (0, name, password, email)
    cursor.execute(qry, val)
    con.commit()

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)

    show()
    messagebox.showinfo("Success", "Data Inserted")


id = 0


def getdata(event):
    global id
    rowid = table.selection()[0]
    data = table.item(rowid)['values']

    id = data[0]

    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)

    e1.insert(0, data[1])
    e2.insert(0, data[2])
    e3.insert(0, data[3])


def deletedata():
    cursor = con.cursor()
    cursor.execute(f"DELETE FROM emp WHERE id={id}")
    con.commit()
    show()
    messagebox.showinfo("Deleted", "Record Deleted")


def updatedata():
    name = e1.get()
    password = e2.get()
    email = e3.get()

    cursor = con.cursor()
    qry = "UPDATE emp SET name=%s, password=%s, email=%s WHERE id=%s"
    val = (name, password, email, id)
    cursor.execute(qry, val)
    con.commit()

    show()
    messagebox.showinfo("Updated", "Record Updated")


Label(root, text="User-Name").place(x=250, y=100)
Label(root, text="Password").place(x=250, y=130)
Label(root, text="Email").place(x=250, y=160)

e1 = Entry(root)
e1.place(x=330, y=100)
e2 = Entry(root)
e2.place(x=330, y=130)
e3 = Entry(root)
e3.place(x=330, y=160)

Button(text="INSERT", command=add_data).place(x=250, y=200)
Button(text="UPDATE", command=updatedata).place(x=320, y=200)
Button(text="DELETE", command=deletedata).place(x=400, y=200)

cols = ("ID", "Name", "Password", "Email")
table = ttk.Treeview(root, columns=cols, show="headings", height=10)

for col in cols:
    table.heading(col, text=col)

table.place(x=10, y=250)

table.bind("<Double-Button-1>", getdata)

show()

root.mainloop()
