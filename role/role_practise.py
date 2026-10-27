import pymysql


def insert(data={}):
    id = data['id']
    name = data['name']
    description = data['description']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "insert into role values(%s, %s, %s)"
    data = (id, name, description)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted successfully')


def update(data={}):
    id = data['id']
    name = data['name']
    description = data['description']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db="advance_python")
    cursor = connection.cursor()
    sql = "update role set name = %s, description = %s where id = %s"
    data = (name, description, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("college updated successfully")


def delete(id):
    connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
    cursor = connection.cursor()
    sql = "delete from role where id = %s"
    data = (id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data deleted successfully")


def get(id):
    connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
    cursor = connection.cursor()
    sql = "select * from role where id = %s"
    data = (id)
    cursor.execute(sql, data)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2])
    connection.commit()
    connection.close()
    print("Data Selected successfully")


def read(data={}):
    id = data.get('id', 0)
    name = data.get('name', 0)
    description = data.get('description', )
    page_no = data.get('page_no', 0)
    page_size = data.get('page_size', 0)

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "select * from role where 1=1"
    if id != 0:
        sql += " and id = " + str(id)
    if name != '':
        sql += " and name = " + str(name)
    if description != '':
        sql += " and description like '" + description + "%'"

    if page_size > 0:
        pageNo = (page_no - 1) * page_size
        sql += " limit " + str(pageNo) + ", " + str(page_size)

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2])
    connection.commit()
    connection.close()


data = {}
data['id'] = 1
data['name'] = 'HR'
data['description'] = 'hiring'
#
# print(data)
insert(data)

# get(id = 1)
# delete(id = 2)
# data['page_no'] = 1
# data['page_size'] = 5
# read(data)
