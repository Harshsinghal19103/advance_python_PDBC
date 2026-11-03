from models.marksheet_model import MarksheetModel
from models.student_model import StudentModel


def do_print(data):
    print(
        data['id'], '\t',
        data['roll_no'], '\t',
        data['name'], '\t',
        data['physics'], '\t',
        data['chemistry'], '\t',
        data['maths'],
    )


def test_add():
    data = {}
    # data['id'] = 8
    data['roll_no'] = 108
    data['physics'] = 70
    data['chemistry'] = 67
    data['maths'] = 79
    data['student_id'] = 1

    student_list = StudentModel().get(data["student_id"])
    first_name = student_list[0].get('first_name')
    last_name = student_list[0].get('last_name')

    data['name'] = first_name + ' ' + last_name

    model = MarksheetModel()
    try:
        model.add(data)
    except Exception as e:
        print(e)


# test_add()

def test_update():
    data = {}
    data['id'] = 2
    data['roll_no'] = 102
    data['physics'] = 76
    data['chemistry'] = 72
    data['maths'] = 89
    data['student_id'] = 2

    student_list = StudentModel().get(data["student_id"])
    first_name = student_list[0].get('first_name')
    last_name = student_list[0].get('last_name')

    data['name'] = first_name + ' ' + last_name

    model = MarksheetModel()
    model.update(data)


# test_update()


def test_delete():
    model = MarksheetModel()
    model.delete(8)


def test_get():
    model = MarksheetModel()
    list = model.get(1)
    for data in list:
        do_print(data)


# test_get()


def test_find_by_roll_no():
    model = MarksheetModel()
    list = model.find_by_roll_no(102)
    for data in list:
        do_print(data)


# test_find_by_roll_no()

def test_search():
    data = {}
    # data['name'] = 'abc'
    # data['roll_no'] = 101
    data['page_no'] = 1
    data['page_size'] = 0
    model = MarksheetModel()
    # models.search(data)
    list = model.search(data)
    for data in list:
        do_print(data)

test_search()
