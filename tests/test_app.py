import json
from registry import data
import logging


def test_get_all(app, client):
    """

    :param app:
    :param client:
    :return:
    """
    res = client.get('/students')
    assert res.status_code == 200
    expected = data.students
    logging.info("expected:{}".format(expected))
    logging.info("actual:{}".format(res.get_data(as_text=True)))
    assert expected == json.loads(res.get_data(as_text=True))


def test_get_by_name(app, client):
    """

    :param app:
    :param client:
    :return:
    """
    name = "ABC"
    res = client.get('/students/bynames?name={}'.format(name))
    total_data = data.students
    logging.info("total_data got:{}".format(total_data))
    expected = None
    for student in total_data:
        if student['name'] == name:
            expected = student
    logging.info("expected:{}".format(expected))
    logging.info("actual:{}".format(res.get_data(as_text=True)))
    assert expected == json.loads(res.get_data(as_text=True))


def test_get_by_id(app, client):
    """
    test the api to get by id
    :param app:
    :param client:
    :return:
    """
    id = 13
    res = client.get('/students/byid?id={}'.format(id))
    total_data = data.students
    logging.info("total_data got:{}".format(total_data))
    expected = None
    for student in total_data:
        if student['id'] == id:
            expected = student
    logging.info("expected:{}".format(expected))
    logging.info("actual:{}".format(res.get_data(as_text=True)))
    assert expected == json.loads(res.get_data(as_text=True))
