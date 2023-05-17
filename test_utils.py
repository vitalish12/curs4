import pytest
from utils import get_data, get_last_values, get_formatted_data

def test_get_data():
    data = get_data()
    assert isinstance(data, list)

def test_get_last_values(test_data):
    data = get_last_values(test_data, 2)
    assert [x["date"] for x in data] == ['2019-12-07T06:17:14.634890', '2019-11-19T09:22:25.899614', '2019-11-13T17:38:04.800051', '2019-10-30T01:49:52.939296', '2019-09-29T14:25:28.588059']

def test_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ['07.12.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD']