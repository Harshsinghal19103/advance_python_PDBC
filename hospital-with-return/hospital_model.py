import pymysql


class HospitalModel:

    def next_pk(self):
        pk = 0
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "select max(id) from hospital"
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
        id = HospitalModel.next_pk(self)
        hospital_name = data['hospital_name']
        city = data['city']
        phone_number = data['phone_number']
        total_beds = data['total_beds']
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "insert into hospital values(%s, %s, %s, %s, %s)"
        data = (id, hospital_name, city, phone_number, total_beds)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data inserted successfully")

    def update(self, data):
        id = data['id']
        hospital_name = data['hospital_name']
        city = data['city']
        phone_number = data['phone_number']
        total_beds = data['total_beds']

        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "update hospital set hospital_name = %s, city = %s, phone_number = %s, total_beds = %s where id = %s"
        data = (hospital_name, city, phone_number, total_beds, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data updated successfully")

    def delete(self, id):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "delete from hospital where id = %s"
        data = (id,)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data deleted successfully")

    def get(self, id):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "select * from hospital where id = %s"
        data = (id,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "hospital_name", "city", "phone_number", "total_beds")
        list = []
        for x in result:
            list.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def find_by_hospital_name(self, hospital_name):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "select * from hospital where hospital_name = %s"
        data = (hospital_name,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "hospital_name", "city", "phone_number", "total_beds")
        list = []
        for x in result:
            list.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def search(self, data):
        id = data.get('id', 0)
        hospital_name = data.get('hospital_name', '')
        city = data.get('city', '')
        phone_number = data.get('phone_number', '')
        total_beds = data.get('total_beds', 0)
        page_no = data.get('page_no', 0)
        page_size = data.get('page_size', 0)

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "select * from hospital where 1=1"
        if id != 0:
            sql += " and id = " + str(id)
        if hospital_name != '':
            sql += " and hospital_name like '" + hospital_name + "%'"
        if city != '':
            sql += " and city like '" + city + "%'"
        if phone_number != '':
            sql += " and phone_number like '" + phone_number + "%'"
        if total_beds != 0:
            sql += " and total_beds = " + str(total_beds)
        if (page_size > 0):
            page_no = (page_no - 1) * page_size
            sql += " limit " + str(page_no) + ", " + str(page_size)
        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        column_name = ("id", "hospital_name", "city", "phone_number", "total_beds")
        list = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list
