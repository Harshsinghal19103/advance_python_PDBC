from student_model import StudentModel
from college_model import CollegeModel
import datetime


def do_print(data):
    print(
        data['id'], '\t',
        data['first_name'], '\t',
        data['last_name'], '\t',
        data['dob'], '\t',
        data['mobile_number'], '\t',
        data['email'], '\t',
        data['college_id'], '\t',
        data['college_name']
    )


def test_add():
    data = {}
    # data['id'] = 1
    data['first_name'] = 'salman'
    data['last_name'] = 'khan'
    data['dob'] = datetime.date(1990, 4, 25)
    data['mobile_number'] = '9496252985'
    data['email'] = 'khan@425'
    data['college_id'] = 1

    college_list = CollegeModel().get(data["college_id"])
    college_name = college_list[0].get('name')
    data['college_name'] = college_name

    student = StudentModel()
    try:
        student.add(data)
    except Exception as e:
        print(e)


test_add()


def test_update():
    data = {}
    data['id'] = 2
    data['first_name'] = 'salman'
    data['last_name'] = 'khan'
    data['dob'] = datetime.date(1990, 4, 25)
    data['mobile_number'] = '9496252985'
    data['email'] = 'khan@425'
    data['college_id'] = 2

    college_list = CollegeModel().get(data["college_id"])
    college_name = college_list[0].get('name')
    data['college_name'] = college_name

    student = StudentModel()
    student.update(data)


# test_update()

def test_delete():
    student = StudentModel()
    student.delete(5)


# test_delete()


def test_get():
    student = StudentModel()
    list = student.get(1)
    for data in list:
        do_print(data)


# test_get()

def test_find_by_email():
    student = StudentModel()
    list = student.find_by_email('khan@425')
    for data in list:
        do_print(data)


# test_find_by_email()

def test_search():
    data = {}
    data['page_no'] = 1
    data['page_size'] = 0
    model = StudentModel()
    list = model.search(data)
    for data in list:
        do_print(data)

# test_search()
