import pymysql

class CollegeModel:

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


    def insert(self, data):
        id = CollegeModel.next_pk(self)
        name = data['name']
        address = data['address']
        state = data['state']
        city = data['city']
        phone_number = data['phone_number']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "insert into college values(%s, %s, %s, %s, %s, %s)"
        data = (id, name, address, state, city, phone_number)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data inserted successfully')


    def update(self,data):
        id = data['id']
        name = data['name']
        address = data['address']
        state = data['state']
        city = data['city']
        phone_number = data['phone_number']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db="advance_python")
        cursor = connection.cursor()
        sql = "update college set name = %s, address = %s, state = %s,city = %s,phone_number = %s where id = %s"
        data = (name, address, state, city, phone_number, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("college updated successfully")


    def delete(self,id):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "delete from college where id = %s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data deleted successfully")


    def get(self,id):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "select * from college where id = %s"
        data = (id)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
        connection.commit()
        connection.close()
        print("Data Selected successfully")


    def read(self,data):
        id = data.get('id', 0)
        name = data.get('name', 0)
        address = data.get('address', '')
        state = data.get('state', 0)
        city = data.get('city', 0)
        phone_number = data.get('phone_number', 0)
        pageNo = data.get('pageNo', 0)
        pageSize = data.get('pageSize', 0)

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "select * from college where 1=1"
        if id != 0:
            sql += " and id = " + str(id)
        if name != 0:
            sql += " and name = " + str(name)
        if address != '':
            sql += " and address like '" + address + "%'"
        if state != 0:
            sql += " and state = " + str(state)
        if city != 0:
            sql += " and city = " + str(city)
        if phone_number != 0:
            sql += " and phone_number = " + str(phone_number)

        if pageSize > 0:
            pageNo = (pageNo - 1) * pageSize
            sql += " limit " + str(pageNo) + ", " + str(pageSize)

        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
        connection.commit()
        connection.close()



