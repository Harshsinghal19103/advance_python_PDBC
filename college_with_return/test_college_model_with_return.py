from college_model_with_return import CollegeModel


def test_add():
    data = {}
    data['id'] = 2
    data['name'] = 'Sage university Bhopal'
    data['address'] = 'sahara bypass'
    data['state'] = 'Madhya Pradesh'
    data['city'] = 'indore'
    data['phone_number'] = '91564616540'

    college = CollegeModel()
    college.insert(data)


# test_add()


def test_update():
    data = {}
    data['id'] = 2
    data['name'] = 'SUB'
    data['address'] = 'sahara bypass'
    data['state'] = 'MP'
    data['city'] = 'indore'
    data['phone_number'] = '8648648481'

    college = CollegeModel()
    college.update(data)


test_update()


def test_get():
    model = CollegeModel()
    list = model.get()
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['address'], '\t', data['state'], '\t', data['city'], '\t',
              data['phone_number'], )


def test_search():
    data = {}
    # data['name'] = 'abc'
    # data['roll_no'] = 101
    data['page_no'] = 1
    data['page_size'] = 0
    model = CollegeModel()
    # model.search(data)
    list = model.search(data)
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['address'], '\t', data['state'], '\t', data['city'], '\t',
              data['phone_number'], )


# test_add()
# test_update()
# test_read()
# test_get()
# test_find_by_roll_no()
test_search()
