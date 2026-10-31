from faculty_model import FacultyModel
import datetime


def test_add():
    data = {}
    # data['id'] = 2
    data['first_name'] = 'neha'
    data['last_name'] = 'gupta'
    data['email'] = 'neha25@gmail.com'
    data['password'] = 'neha@123'
    data['address'] = 'rajendra nagar'
    data['gender'] = 'Female'
    data['dob'] = datetime.date(2001, 11, 5)
    data['college_id'] = 2
    data['course_id'] = 3
    data['subject_id'] = 6

    faculty = FacultyModel()
    # faculty.add(data)
    try:
        faculty.add(data)
    except Exception as e:
        print(e)


test_add()


def test_update():
    data = {}
    data['id'] = 2
    data['first_name'] = 'amit'
    data['last_name'] = 'sharma'
    data['email'] = 'amit21@gmail.com'
    data['password'] = 'amit@123'
    data['address'] = 'vijay nagar'
    data['gender'] = 'Male'
    data['dob'] = datetime.date(2001, 5, 15)
    data['college_id'] = 2
    data['course_id'] = 1
    data['subject_id'] = 2

    faculty = FacultyModel()
    faculty.update(data)


# test_update()

def test_delete():
    user = FacultyModel()
    user.delete(5)


# test_delete()

def test_get():
    user = FacultyModel()
    list = user.get(5)
    for data in list:
        print(data['id'], '\t', data['first_name'], '\t', data['last_name'], '\t', data['email'], '\t',
              data['password'], '\t', data['address'], '\t', data['gender'], '\t', data['dob'], '\t',
              data['college_id'], '\t', data['course_id'], '\t', data['subject_id'], )


# test_get()

def test_find_by_email():
    faculty = FacultyModel()
    list = faculty.find_by_email('amit21@gmail.com')
    for data in list:
        print(data['id'], '\t', data['first_name'], '\t', data['last_name'], '\t', data['email'], '\t',
              data['password'], '\t', data['address'], '\t', data['gender'], '\t', data['dob'], '\t',
              data['college_id'], '\t', data['course_id'], '\t', data['subject_id'], )


# test_find_by_email()

def test_search():
    data = {}
    data['page_no'] = 1
    data['page_size'] = 0
    model = FacultyModel()
    # model.search(data)
    list = model.search(data)
    for data in list:
        print(
              data['id'], '\t',
              data['first_name'], '\t',
              data['last_name'], '\t',
              data['email'], '\t',
              data['password'], '\t',
              data['address'], '\t',
              data['gender'], '\t',
              data['dob'], '\t',
              data['college_id'], '\t',
              data['course_id'], '\t',
              data['subject_id'],
              )

# test_search()
