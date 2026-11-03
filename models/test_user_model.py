from models.role_model import RoleModel
from user_model import UserModel
import datetime

def do_print(data):
    print(
        data['id'], '\t',
        data['first_name'], '\t',
        data['last_name'], '\t',
        data['login_id'], '\t',
        data['password'], '\t',
        data['dob'], '\t',
        data['address'], '\t',
        data['role_id'], '\t',
        data['role_name']
    )

def test_add():
    data = {}
    # data['id'] = 2
    data['first_name'] = 'rahul'
    data['last_name'] = 'kumar'
    data['login_id'] = 'kumar18'
    data['password'] = 'kumar@#18'
    data['dob'] = datetime.date(2000,12,20)
    data['address'] = 'lal bagh'
    data['role_id'] = 1

    role_list = RoleModel().get(data["role_id"])
    role_name = role_list[0].get('name')
    data['role_name'] = role_name

    user = UserModel()
    try:
        user.add(data)
    except Exception as e:
        print(e)

# test_add()

def test_update():
    data = {}
    data['id'] = 4
    data['first_name'] = 'rahul'
    data['last_name'] = 'kumar'
    data['login_id'] = 'kumar18'
    data['password'] = 'kumar@#18'
    data['dob'] = datetime.date(2000,12,20)
    data['address'] = 'lal bagh'
    data['role_id'] = 3

    role_list = RoleModel().get(data["role_id"])
    role_name = role_list[0].get('name')
    data['role_name'] = role_name

    user = UserModel()
    user.update(data)

# test_update()

def test_delete():
    user = UserModel()
    user.delete(8)



def test_get():
    user = UserModel()
    list = user.get()
    for data in list:
        do_print(data)


def test_find_by_login_id():
    user = UserModel()
    list = user.find_by_login_id(103)
    for data in list:
        do_print(data)


def test_search():
    data = {}
    data['page_no'] = 1
    data['page_size'] = 0
    model = UserModel()
    # models.search(data)
    list = model.search(data)
    for data in list:
        do_print(data)





# test_read()
# test_get()
# test_delete()
test_search()