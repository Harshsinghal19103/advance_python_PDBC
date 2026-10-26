import pymysql

connection = pymysql.Connection(host = "localhost",port = 3306,user = "root",password ="root",db = "advance_python")
cursor = connection.cursor()
sql = "select * from college"
cursor.execute(sql)
result = cursor.fetchall()
for data in result:
    print(data[0],data[1],data[2],data[3],data[4],data[5])
connection.close()
print("selected successfully")