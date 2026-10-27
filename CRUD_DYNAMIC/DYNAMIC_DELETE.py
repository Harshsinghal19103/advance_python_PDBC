import pymysql


def test_delete_01():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "delete from marksheet where id = 4"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print('data deleted successfully')


def test_delete_02():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "delete from marksheet where id = %s"
    data = (2)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data deleted successfully')


def test_delete_03(id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advance_python')
    cursor = connection.cursor()
    sql = "delete from marksheet where id = %s"
    data = (id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data deleted successfully')

test_delete_01()
# test_delete_02()
# test_delete_03(3)