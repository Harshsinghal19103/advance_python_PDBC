import pymysql


class Marksheet_Model():


    def add(self, data):
        id = data['id']
        rollNo = data['rollno']
        name = data['name']
        physics = data['physics']
        chemistry = data['chemistry']
        maths = data['maths']
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s)"
        data = (id, rollNo, name, physics, chemistry, maths)
        cursor.execute(sql,data)
        connection.commit()
        connection.close()
        print("Data inserted successfully")



    def update(self, data):
        id = data['id']
        rollNo = data['rollno']
        name = data['name']
        physics = data['physics']
        chemistry = data['chemistry']
        maths = data['maths']
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "update marksheet set rollno = %s, name = %s, physics = %s, chemistry = %s, maths = %s where id = %s"
        data = (id, rollNo, name, physics, chemistry, maths)
        cursor.execute(sql,data)
        connection.commit()
        connection.close()
        print("Data updated successfully")




    def delete(self, id):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "delete from marksheet where id = %s"
        data = (id)
        cursor.execute(sql,data)
        connection.commit()
        connection.close()
        print("Data deleted successfully")



    def get(self, id):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "select from marksheet where id = %s"
        data = (id)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
        connection.commit()
        connection.close()
        print("Data Selected successfully")



    def find_by_rollno(self, rollNo):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "select from marksheet where rollNo = %s"
        data = (rollNo)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
        connection.commit()
        connection.close()
        print("Data Selected successfully")





