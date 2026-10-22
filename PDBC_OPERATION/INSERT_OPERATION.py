import pymysql

connection = pymysql.Connection(host = "localhost",port = 3306,user = "root",password ="root",db = "advance_python")
cursor = connection.cursor()
sql = "insert into student values(101,'harsh',97)"
sql = "insert into student values(102,'vansh',95)"
sql = "insert into student values(103,'max',89)"
cursor.execute(sql)
connection.commit()
connection.close()
print("inserted successfully")