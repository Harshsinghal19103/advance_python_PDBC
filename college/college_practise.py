import pymysql


def insert(data = {}):
    id = data['id']
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


def update(data={}):
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


def delete(id):
    connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root", db="advance_python")
    cursor = connection.cursor()
    sql = "delete from college where id = %s"
    data = (id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data deleted successfully")


def get(id):
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


def read(data={}):
    id = data.get('id', 0)
    name = data.get('name', '')
    address = data.get('address', '')
    state = data.get('state', '')
    city = data.get('city', '')
    phone_number = data.get('phone_number', '')
    page_no = data.get('page_no', 0)
    page_size = data.get('page_size', 0)

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

    if page_size > 0:
        pageNo = (page_no - 1) * page_size
        sql += " limit " + str(pageNo) + ", " + str(page_size)

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()


data = {}
# data['id'] = 1
# data['name'] = 'IIT Indore'
# data['address'] = 'Chanhni chowk'
# data['state'] = 'Madhya pradesh'
# data['city'] = 'indore'
# data['phone_number'] = '9654681165'
#
# print(data)
# Insert(data)

# get(id = 1)
# delete(id = 2)
data['page_no'] = 1
data['page_size'] = 5
read(data)