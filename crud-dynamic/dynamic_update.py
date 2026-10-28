import pymysql


def Test_update_01():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db="advance_python")
    cursor = connection.cursor()
    sql = "update marksheet set chemistry = 67,maths = 72, physics= 88 where id = 3"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("marksheet updated successfully")


def Test_update_02():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db="advance_python")
    cursor = connection.cursor()
    sql = "update marksheet set chemistry = %s,maths = %s where id = %s"
    data = (54, 72, 5)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("marksheet updated successfully")


def Test_update_03(roll_no, name, physics, chemistry, maths, id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db="advance_python")
    cursor = connection.cursor()
    sql = "update marksheet set rollno = %s, name = %s, physics = %s,chemistry = %s,maths = %s where id = %s"
    data = (roll_no, name, physics, chemistry, maths, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("marksheet updated successfully")


def Test_update_04(data={}):
    id = data['id']
    roll_no = data['roll_no']
    name = data['name']
    physics = data['physics']
    chemistry = data['chemistry']
    maths = data['maths']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db="advance_python")
    cursor = connection.cursor()
    sql = "update marksheet set roll_no = %s, name = %s, physics = %s,chemistry = %s,maths = %s where id = %s"
    data = (roll_no, name, physics, chemistry, maths, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("marksheet updated successfully")


# Test_update_01()
Test_update_02()
# Test_update_03(106,'harsh',87,92,97,2)

# data = {}
# data['id'] = 3
# data['roll_no'] = 103
# data['name'] = 'vansh'
# data['physics'] = 78
# data['chemistry'] = 72
# data['maths'] = 75
#
# Test_update_04(data)
