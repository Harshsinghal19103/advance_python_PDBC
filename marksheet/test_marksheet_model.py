from marksheet_model import MarksheetModel

def test_add():
    data = {}
    data['id'] = 6
    data['roll_no'] = 106
    data['name'] = 'pranjay'
    data['physics'] = 89
    data['chemistry'] = 99
    data['maths'] = 90

    marksheet = MarksheetModel()
    marksheet.add(data)

# test_add()


def test_update():
    data = {}
    data['id'] = 5
    data['roll_no'] = 105
    data['name'] = 'manish'
    data['physics'] = 56
    data['chemistry'] = 78
    data['maths'] = 85

    marksheet= MarksheetModel()
    marksheet.update(data)

test_update()

def test_delete():
    marksheet= MarksheetModel()
    marksheet.delete(1)

# test_delete()


def test_get():
    marksheet = MarksheetModel()
    marksheet.get(2)


def test_find_by_roll_no():
    marksheet = MarksheetModel()
    marksheet.find_by_roll_no(102)


