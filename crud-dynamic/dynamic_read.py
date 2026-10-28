import pymysql


def test_read_1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "select * from marksheet"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()


def test_read_2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "select * from marksheet"
    cursor.execute(sql)
    result = cursor.fetchall()
    columnName = ("id", "roll_no", "name", "physics", "chemistry", "maths")
    for x in result:
        print({columnName[i]: x[i] for i, _ in enumerate(x)})
    connection.commit()
    connection.close()


def test_read_3():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()

    # sql = "select * from marksheet"
    sql = "select * from marksheet where id = 1"
    # sql = "select * from marksheet where roll_no = 101"
    # sql = "select * from marksheet where name like 'a%'"
    # sql = "select * from marksheet where physics = 12"
    # sql = "select * from marksheet where chemistry = 34"
    # sql = "select * from marksheet where maths = 55"

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()


def test_read_4(id, roll_no, name, physics, chemistry, maths):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()

    sql = 'select * from marksheet'
    if id != 0:
        sql += " where id = " + str(id)
    if roll_no != 0:
        sql += " where roll_no = " + str(roll_no)
    if name != '':
        sql += " where name like '" + name + "%'"
    if physics != 0:
        sql += " where physics = " + str(physics)
    if chemistry != 0:
        sql += " where chemistry = " + str(chemistry)
    if maths != 0:
        sql += " where maths = " + str(maths)
    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()


def test_read_5(param={}):
    id = param.get('id', 0)
    roll_no = param.get('roll_no', 0)
    name = param.get('name', '')
    physics = param.get('physics', 0)
    chemistry = param.get('chemistry', 0)
    maths = param.get('maths', 0)

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "select * from marksheet where 1=1"
    if id != 0:
        sql += " and id = " + str(id)
    if roll_no != 0:
        sql += " and roll_no = " + str(roll_no)
    if name != '':
        sql += " and name like '" + name + "%'"
    if physics != 0:
        sql += " and physics = " + str(physics)
    if chemistry != 0:
        sql += " and chemistry = " + str(chemistry)
    if maths != 0:
        sql += " and maths = " + str(maths)

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()


def test_read_6(param={}):
    id = param.get('id', 0)
    roll_no = param.get('roll_no', 0)
    name = param.get('name', '')
    physics = param.get('physics', 0)
    chemistry = param.get('chemistry', 0)
    maths = param.get('maths', 0)
    page_no = param.get('page_no', 0)
    page_size = param.get('page_size', 0)

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "select * from marksheet where 1=1"
    if id != 0:
        sql += " and id = " + str(id)
    if roll_no != 0:
        sql += " and roll_no = " + str(roll_no)
    if name != '':
        sql += " and name like '" + name + "%'"
    if physics != 0:
        sql += " and physics = " + str(physics)
    if chemistry != 0:
        sql += " and chemistry = " + str(chemistry)
    if maths != 0:
        sql += " and maths = " + str(maths)

    if page_size > 0:
        pageNo = (page_no - 1) * page_size
        sql += " limit " + str(page_no) + ", " + str(page_size)

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()


# testRead1()
# testRead2()
# testRead3()
# testRead4(1, 101, '', 0, 0, 0)

param = {}
param['name'] = 'a'
param['roll_no'] = 101
param['page_no'] = 1
param['page_size'] = 5

# test_read_5(param)

test_read_6(param)