from college_model import CollegeModel

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
