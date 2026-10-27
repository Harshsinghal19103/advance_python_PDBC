from marksheet_model_with_return import MarksheetModel


def test_add():
    data = {}
    # data['id'] = 8
    data['roll_no'] = 108
    data['name'] = 'abc'
    data['physics'] = 70
    data['chemistry'] = 67
    data['maths'] = 79

    model = MarksheetModel()
    model.add(data)


def test_update():
    data = {}
    data['id'] = 8
    data['roll_no'] = 108
    data['name'] = 'ooo'
    data['physics'] = 70
    data['chemistry'] = 67
    data['maths'] = 79

    model = MarksheetModel()
    model.update(data)


def test_delete():
    model = MarksheetModel()
    model.delete(8)


def test_read():
    model = MarksheetModel()
    model.read()


def test_get():
    model = MarksheetModel()
    list = model.get()
    for data in list:
        print(data['id'], '\t', data['roll_no'], '\t', data['name'], '\t', data['physics'], '\t', data['chemistry'],
              '\t',
              data['maths'], )


def test_find_by_roll_no():
    model = MarksheetModel()
    list = model.find_by_roll_no(103)
    for data in list:
        print(data['id'], '\t', data['roll_no'], '\t', data['name'], '\t', data['physics'], '\t', data['chemistry'],
              '\t',
              data['maths'], )


def test_search():
    data = {}
    # data['name'] = 'abc'
    # data['roll_no'] = 101
    data['page_no'] = 1
    data['page_size'] = 0
    model = MarksheetModel()
    # model.search(data)
    list = model.search(data)
    for data in list:
        print(data['id'], '\t', data['roll_no'], '\t', data['name'], '\t', data['physics'], '\t', data['chemistry'],
              '\t', data['maths'], )


# test_add()
# test_update()
# test_read()
# test_get()
# test_find_by_roll_no()
test_search()
