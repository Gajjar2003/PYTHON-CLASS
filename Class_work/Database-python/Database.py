import mysql.connector as sql

con = sql.connect (
    host = "localhost",
    user = "root",
    password = "Admin@123",
    port = 3306,
    database = "pythonsql"
    

)

cursor = con.cursor()
# print(" ********************************* carete batabase quary ***************************************************")

# cursor.execute("create database pythonsql")


# print(" ********************************* carete table quary ***************************************************")

# cursor.execute("create table emp(id int primary key,name varchar(20),email varchar(50))")

# print(" ********************************* carete insert quary ***************************************************")

# cursor.execute("insert into emp values(3,'Jenil','jenil@gmail.com')")
# cursor.execute("insert into emp values(1,'om','om@gmail.com')")
# cursor.execute("insert into emp values(2,'meet','meet@gmail.com')")
# cursor.execute("insert into emp values(4,'yug','yug@gmail.com')")


# print(" ********************************* carete upadte quary ***************************************************")

# cursor.execute("update emp set email='abc@gmail.com' where id = 3")

# print(" ********************************* carete detele quary ***************************************************")

# cursor.execute("delete from emp where id=3")

con.commit()    

cursor.execute("select * from emp")

data = cursor.fetchall()  

print(data)