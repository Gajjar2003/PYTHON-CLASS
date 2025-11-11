# Write a Python program to connect to an SQLite3 database, create a table, insert data, and fetch data.

import sqlite3


con = sqlite3.connect("mydatabase.db")

cur = con.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
);
""")


cur.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Jenil", 21))
cur.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Om", 22))


con.commit()


cur.execute("SELECT * FROM students")
rows = cur.fetchall()


for row in rows:
    print(row)


con.close()
