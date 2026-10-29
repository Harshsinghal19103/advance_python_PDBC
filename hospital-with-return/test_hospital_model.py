from hospital_model import HospitalModel


def test_add():
    data = {}
    # data['id'] = 2
    data['hospital_name'] = 'Care Plus Hospital'
    data['city'] = 'Nagpur'
    data['phone_number'] = '9876543219 110'
    data['total_beds'] = 110

    college = HospitalModel()
    college.add(data)


def test_update():
    data = {}
    data['id'] = 2
    data['hospital_name'] = 'LifeLine Hospital'
    data['city'] = 'Mumbai'
    data['phone_number'] = '9876543212'
    data['total_beds'] = 100

    college = HospitalModel()
    college.update(data)


def test_delete():
    model = HospitalModel()
    model.delete(8)


def test_get():
    model = HospitalModel()
    list = model.get(5)
    for data in list:
        print(data['id'], '\t', data['hospital_name'], '\t', data['phone_number'], '\t', data['city'], '\t',
              data['total_beds'], '\t', )


def test_find_by_hospital_name():
    model = HospitalModel()
    list = model.find_by_hospital_name('Apollo Hospital')
    for data in list:
        print(data['id'], '\t', data['hospital_name'], '\t', data['phone_number'], '\t', data['city'], '\t',
              data['total_beds'], '\t', )


def test_search():
    data = {}
    # data['hospital_name'] = 'abc'
    data['page_no'] = 1
    data['page_size'] = 0
    model = HospitalModel()
    # model.search(data)
    list = model.search(data)
    for data in list:
        print(data['id'], '\t', data['hospital_name'], '\t', data['phone_number'], '\t', data['city'], '\t',
              data['total_beds'], '\t', )


# test_add()
# test_update()
test_delete()
# test_get()
# test_find_by_hospital_name()
# test_search()
