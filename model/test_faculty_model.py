from faculty_model import FacultyModel
import datetime

from model.college_model import CollegeModel
from model.course_model import CourseModel
from model.subject_model import SubjectModel


def do_print(data):
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
        data['college_name'], '\t',
        data['course_id'], '\t',
        data['course_name'], '\t',
        data['subject_id'], '\t',
        data['subject_name']
    )


def test_add():
    data = {}
    # data['id'] = 2
    data['first_name'] = 'rakesh'
    data['last_name'] = 'panchal'
    data['email'] = 'rakesh123@gmail.com'
    data['password'] = 'rakesh@123'
    data['address'] = 'chandni chowk'
    data['gender'] = 'male'
    data['dob'] = datetime.date(1993, 11, 5)
    data['college_id'] = 3
    data['course_id'] = 1
    data['subject_id'] = 1

    college_list = CollegeModel().get(data["college_id"])
    college_name = college_list[0].get('name')
    data['college_name'] = college_name

    course_list = CourseModel().get(data["course_id"])
    course_name = course_list[0].get('name')
    data['course_name'] = course_name

    subject_list = SubjectModel().get(data["subject_id"])
    subject_name = subject_list[0].get('name')
    data['subject_name'] = subject_name

    faculty = FacultyModel()
    try:
        faculty.add(data)
    except Exception as e:
        print(e)


# test_add()


def test_update():
    data = {}
    data['id'] = 3
    data['first_name'] = 'priya'
    data['last_name'] = 'verma'
    data['email'] = 'priya23@gmail.com'
    data['password'] = 'priya@123'
    data['address'] = 'palasia'
    data['gender'] = 'Female'
    data['dob'] = datetime.date(2002, 3, 10)
    data['college_id'] = 1
    data['course_id'] = 2
    data['subject_id'] = 5

    college_list = CollegeModel().get(data["college_id"])
    college_name = college_list[0].get('name')
    data['college_name'] = college_name

    course_list = CourseModel().get(data["course_id"])
    course_name = course_list[0].get('name')
    data['course_name'] = course_name

    subject_list = SubjectModel().get(data["subject_id"])
    subject_name = subject_list[0].get('name')
    data['subject_name'] = subject_name

    faculty = FacultyModel()
    faculty.update(data)


# test_update()


def test_delete():
    faculty = FacultyModel()
    faculty.delete(5)


# test_delete()

def test_get():
    faculty = FacultyModel()
    list = faculty.get(1)
    for data in list:
        do_print(data)


test_get()

def test_find_by_email():
    faculty = FacultyModel()
    list = faculty.find_by_email('amit21@gmail.com')
    for data in list:
        do_print(data)


# test_find_by_email()

def test_search():
    data = {}
    data['page_no'] = 1
    data['page_size'] = 0
    model = FacultyModel()
    # model.search(data)
    list = model.search(data)
    for data in list:
        # college_list = CollegeModel().get(data["college_id"])
        # college_name = college_list[0].get('name')
        #
        # course_list = CourseModel().get(data["college_id"])
        # course_name = course_list[0].get('name')
        #
        # subject_list = SubjectModel().get(data["college_id"])
        # subject_name = subject_list[0].get('name')

        do_print(data)

# test_search()
