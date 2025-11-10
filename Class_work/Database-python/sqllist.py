import sqlite3

db = sqlite3.connect("data.db")

# db.execute("create table emp(id int primary key,name varchar(20),email varchar(50))")

# db.execute("insert into emp values(3,'Jenil','jenil@gmail.com')")


# db.execute("update emp set email='abc@gmail.com' where id = 3")

# db.execute("delete from emp where id=3")

db.commit()
data = db.execute("select * from emp").fetchall()
for dt in data:
    print(dt)