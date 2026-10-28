import pymysql

connection = pymysql.Connection(host = "localhost",port = 3306,user = "root",password ="root",db = "advance_python")
cursor = connection.cursor()
sql = "delete from student where id = 103"
cursor.execute(sql)
connection.commit()
connection.close()
print("deleted successfully")