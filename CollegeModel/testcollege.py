from College_Model import College_Model

def add():
    data = {}
    data['id'] = 2
    data['name'] = 'Sage university Bhopal'
    data['address'] = 'sahara bypass'
    data['state'] = 'Madhya Pradesh'
    data['city'] = 'indore'
    data['phone_number'] = '91564616540'

    test = College_Model()
    test.Insert(data)

add()