import pymysql

connection = pymysql.Connection(host = "localhost",port = 3306,user = "root",password ="root",db = "advance_python")
cursor = connection.cursor()
sql = "update college set name = 'SUB' where id = 3"
cursor.execute(sql)
connection.commit()
connection.close()
print("updated successfully")