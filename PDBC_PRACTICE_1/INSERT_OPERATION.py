import pymysql

connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
cursor = connection.cursor()
# sql = "insert into college values(1,'Sage University Indore','rau bypass','Madhya Pradesh','Indore',9659245154)"
# sql = "insert into college values(2,'NIT Bhopal','Main road no 3','Madhya Pradesh','Bhopal','9161551981')"
sql = "insert into college values(3,'Sage University Bhopal','rau bypass','Madhya Pradesh','Bhopal',9855195129)"
# sql = "insert into college values(4,'MIT Ujjain','dewas road','Madhya Pradesh','Ujjain',9519153151)"
cursor.execute(sql)
connection.commit()
connection.close()
print("inserted successfully")
