from user_model import UserModel
import datetime

def test_add():
    data = {}
    # data['id'] = 2
    data['first_name'] = 'rahul'
    data['last_name'] = 'lu'
    data['login_id'] = 'prerna03'
    data['password'] = 'prerna@#03'
    data['dob'] = datetime.date(2005,10,31)
    data['address'] = 'rani bagh'

    user = UserModel()
    user.add(data)

test_add()

def test_update():
    data = {}
    data['id'] = 2
    data['first_name'] = 'Sage university Bhopal'
    data['last_name'] = 'sahara bypass'
    data['login_id'] = 'Madhya Pradesh'
    data['password'] = 'indore'
    data['dob'] = '91564616540'
    data['address'] = '91564616540'

    user = UserModel()
    user.update(data)


def test_delete():
    user = UserModel()
    user.delete(8)



def test_get():
    user = UserModel()
    list = user.get()
    for data in list:
        print(data['id'], '\t', data['first_name'], '\t', data['last_name'], '\t', data['login_id'], '\t', data['password'],
              '\t', data['dob'], '\t', data['address'], )


def test_find_by_login_id():
    user = UserModel()
    list = user.find_by_login_id(103)
    for data in list:
        print(data['id'], '\t', data['first_name'], '\t', data['last_name'], '\t', data['login_id'], '\t',
              data['password'], '\t', data['dob'], '\t', data['address'], )


def test_search():
    data = {}
    # data['name'] = 'abc'
    # data['roll_no'] = 101
    data['page_no'] = 1
    data['page_size'] = 0
    model = UserModel()
    # model.search(data)
    list = model.search(data)
    for data in list:
        print(data['id'], '\t', data['first_name'], '\t', data['last_name'], '\t', data['login_id'], '\t',
              data['password'], '\t', data['dob'], '\t', data['address'], )



# test_update()
# test_read()
# test_get()
# test_delete()
# test_search()