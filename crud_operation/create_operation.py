import pymysql

# connection = pymysql.Connection(host = "localhost",port = 3306,user = "root",password ="root",db = "advance_python")
# cursor = connection.cursor()
# sql = "create table student(id int primary key,name varchar(50),marks int)"
# cursor.execute(sql)
# connection.commit()
# connection.close()
# print("created successfully")



# connection = pymysql.Connection(host = "localhost",port = 3306,user = "root",password ="root",db = "advance_python")
# cursor = connection.cursor()
# sql = "create table marksheet(id int primary key, rollNo int, name varchar(50), physics int, chemistry int, maths int)"
# cursor.execute(sql)
# connection.commit()
# connection.close()
# print("created successfully")


connection = pymysql.Connection(host = "localhost",port = 3306,user = "root",password ="root",db = "advance_python")
cursor = connection.cursor()
sql = "create table role(id int primary key, name varchar(50), description varchar(50) )"
cursor.execute(sql)
connection.commit()
connection.close()
print("created successfully")