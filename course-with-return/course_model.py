import pymysql


class CourseModel:

    def add(self, data):
        name = data['name']
        description = data['description']
        duration = data['duration']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "insert into course values(%s, %s, %s)"
        data = (name, description, duration)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data inserted successfully')

    def update(self, data):
        name = data['name']
        description = data['description']
        duration = data['duration']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db="advance_python")
        cursor = connection.cursor()
        sql = "update course set description = %s, duration = %s where name = %s"
        data = (description, duration, name)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("college updated successfully")

    def delete(self, name):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "delete from course where name = %s"
        data = (name)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data deleted successfully")

    def get(self, name):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
        cursor = connection.cursor()
        sql = "select * from course where name = %s"
        data = (name)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ("name", "description", "duration")
        list = []
        for x in result:
            # print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def search(self, data):
        name = data.get('name', '')
        description = data.get('description', '')
        duration = data.get('duration', '')
        page_no = data.get('page_no', 0)
        page_size = data.get('page_size', 0)

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
        cursor = connection.cursor()
        sql = "select * from course where 1=1"
        if name != '':
            sql += " and name like '" + name + "%'"
        if description != '':
            sql += " and description like '" + description + "%'"
        if duration != '':
            sql += " and duration like '" + duration + "%'"

        if page_size > 0:
            page_no = (page_no - 1) * page_size
            sql += " limit " + str(page_no) + ", " + str(page_size)

        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        column_name = ("name", "description", "duration")
        list = []
        for x in result:
            # print({columnName[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list
