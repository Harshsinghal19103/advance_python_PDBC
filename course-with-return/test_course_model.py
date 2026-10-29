from course_model import CourseModel


def test_add():
    data = {}
    data['name'] = 'C'
    data['description'] = 'C programming fundamental'
    data['duration'] = '6 month'
    course = CourseModel()
    course.add(data)


# test_add()

def test_update():
    data = {}
    data['name'] = 'Python'
    data['description'] = 'Python programming advance'
    data['duration'] = ''
    course = CourseModel()
    course.update(data)


def test_delete():
    course = CourseModel()
    course.delete('C')


def test_get():
    course = CourseModel()
    list = course.get('AWS')
    for data in list:
        print(data['name'], '\t', data['description'], '\t', data['duration'], )


def test_search():
    data = {}
    # data['name'] = 'abc'
    data['page_no'] = 1
    data['page_size'] = 0
    model = CourseModel()
    # model.search(data)
    list = model.search(data)
    for data in list:
        print(data['name'], '\t', data['description'], '\t', data['duration'], )


# test_add()
# test_update()
# test_read()
test_get()
# test_delete()
# test_search()
