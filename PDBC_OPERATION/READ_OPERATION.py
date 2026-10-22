import pymysql

connection = pymysql.Connection(host = "localhost",port = 3306,user = "root",password ="root",db = "advance_python")
cursor = connection.cursor()
sql = "select * from student"
cursor.execute(sql)
result = cursor.fetchall()
for data in result:
    print(data[0],data[1],data[2])
connection.close()
print("selected successfully")