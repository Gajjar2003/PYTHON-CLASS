import mysql.connector as sql

con = sql.connect(
    host="localhost",
    user="root",
    password="Admin@123",
    port=3306,
    database = "jenilsql"
)

cursor = con.cursor()

# cursor.execute("create database jenilsql")

# cursor.execute("create table stu(id int primary key,name varchar(30),email varchar(30),subject varchar(30))")

# cursor.execute("insert into stu values (1,'jenil','Jenil@gamil.com','html')")
# cursor.execute("insert into stu values (2,'yug','yug@gamil.com','python')")
# cursor.execute("insert into stu values (3,'meet','meet@gamil.com','css')")
# cursor.execute("insert into stu values (4,'janvi','janvi@gamil.com','java')")
# cursor.execute("insert into stu values (5,'bhumi','bhumi@gamil.com','c++')")


# cursor.execute("update stu set email='abc@gmail.com' where id = 1")

# cursor.execute("select * from stu")



# data = cursor.fetchall()  

# print(data)