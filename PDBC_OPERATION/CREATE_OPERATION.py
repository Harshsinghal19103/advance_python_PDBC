import pymysql

connection = pymysql.Connection(host = "localhost",port = 3306,user = "root",password ="root",db = "advance_python")
cursor = connection.cursor()
sql = "create table student(id int primary key,name varchar(50),marks int)"
cursor.execute(sql)
connection.commit()
connection.close()
print("created successfully")