from role_model import RoleModel


def test_add():
    data = {}
    # data['id'] =
    data['name'] = 'Accountant'
    data['description'] = 'Manages financial records'
    role = RoleModel()
    role.insert(data)


test_add()


def test_update():
    data = {}
    data['id'] = 2
    data['name'] = 'Admin'
    data['description'] = 'administrator'
    role = RoleModel()
    role.update(data)


# test_update()

def test_delete():
    role = RoleModel()
    role.delete(1)


# test_delete()


def test_get():
    role = RoleModel()
    role.get(2)


def test_find_by_roll_no():
    role = RoleModel()
    role.find_by_roll_no(102)
