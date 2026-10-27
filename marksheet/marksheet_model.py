import pymysql


class MarksheetModel:

    def next_pk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "select max(id) from marksheet"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()

        return pk + 1

    def add(self, data):
        id = MarksheetModel.next_pk(self)
        roll_no = data['roll_no']
        name = data['name']
        physics = data['physics']
        chemistry = data['chemistry']
        maths = data['maths']
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s)"
        data = (id, roll_no, name, physics, chemistry, maths)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data inserted successfully")

    def update(self, data):
        id = data['id']
        roll_no = data['roll_no']
        name = data['name']
        physics = data['physics']
        chemistry = data['chemistry']
        maths = data['maths']
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "update marksheet set roll_no = %s, name = %s, physics = %s, chemistry = %s, maths = %s where id = %s"
        data = (roll_no, name, physics, chemistry, maths, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data updated successfully")

    def delete(self, id):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "delete from marksheet where id = %s"
        data = (id)
        cursor.execute(sql, data)
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

    def find_by_roll_no(self, roll_no):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "select from marksheet where roll_no = %s"
        data = (roll_no)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
        connection.commit()
        connection.close()
        print("Data Selected successfully")
