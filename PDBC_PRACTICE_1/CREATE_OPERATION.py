import pymysql

connection = pymysql.Connection(host = "localhost",port = 3306,user = "root",password ="root",db = "advance_python")
cursor = connection.cursor()
sql = "create table college(id int primary key, name varchar(50),address varchar(50), state varchar(50), city varchar(50), phone_number varchar(50))"
cursor.execute(sql)
connection.commit()
connection.close()
print("created successfully")