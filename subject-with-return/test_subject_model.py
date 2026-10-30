from subject_model import SubjectModel


def test_add():
    data = {}
    # data['id'] = 3
    data['name'] = 'core java'
    data['description'] = 'basics, oop, file-handling'
    data['course_id'] = 2
    subject = SubjectModel()
    # subject.add(data)
    try:
        subject.add(data)
    except Exception as e:
        print(e)


test_add()

def test_update():
    data = {}
    data['id'] = 1
    data['name'] = 'core python'
    data['description'] = 'data type, oop, threading, file-handling '
    data['course_id'] = 1
    subject = SubjectModel()
    subject.update(data)


# test_update()


def test_delete():
    subject = SubjectModel()
    subject.delete(3)


# test_delete()

def test_search():
    data = {}
    # data['name'] = 'abc'
    data['page_no'] = 1
    data['page_size'] = 0
    model = SubjectModel()
    # model.search(data)
    list = model.search(data)
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['description'], '\t', data['course_id'], )


# test_search()

def test_get():
    subject = SubjectModel()
    list = subject.get(2)
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['description'], '\t', data['course_id'], )


# test_get()

def test_find_by_name():
    subject = SubjectModel()
    list = subject.find_by_name('core python')
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['description'], '\t', data['course_id'], )

# test_find_by_name()
