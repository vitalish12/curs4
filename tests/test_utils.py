import pytest
from utils import get_data, get_last_values, get_formatted_data

@pytest.fixture
def test_data():
    return [
        {'date': '2019-12-07T06:17:14.634890',
         'description': 'Перевод организации',
         'from': 'Visa Classic 2842878893689012',
         'operationAmount': {'amount': '48150.39',
                             'currency': {'name': 'USD', 'code': 'USD'}},
         'to': 'Счет 35158586384610753655'},
        {'id': 154927927,
         'state': 'EXECUTED',
         'date': '2019-11-19T09:22:25.899614',
         'operationAmount': {'amount': '30153.72',
                             'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод организации',
         'from': 'Maestro 7810846596785568',
         'to': 'Счет 43241152692663622869'},
        {'id': 482520625, 'state': 'EXECUTED',
         'date': '2019-11-13T17:38:04.800051',
         'operationAmount': {'amount': '62814.53',
                             'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод со счета на счет',
         'from': 'Счет 38611439522855669794',
         'to': 'Счет 46765464282437878125'},
        {'id': 509645757,
         'state': 'EXECUTED',
         'date': '2019-10-30T01:49:52.939296',
         'operationAmount': {'amount': '23036.03',
                             'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод с карты на счет',
         'from': 'Visa Gold 7756673469642839',
         'to': 'Счет 48943806953649539453'},
        {'id': 888407131,
         'state': 'EXECUTED',
         'date': '2019-09-29T14:25:28.588059',
         'operationAmount': {'amount': '45849.53',
                             'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод со счета на счет',
         'from': 'Счет 35421428450077339637',
         'to': 'Счет 46723050671868944961'}]

def test_get_data():
    data = get_data()
    assert isinstance(data, list)

def test_get_last_values(test_data):
    data = get_last_values(test_data, 2)
    assert [x["date"] for x in data] == ['2019-12-07T06:17:14.634890', '2019-11-19T09:22:25.899614']

def test_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ['07.12.2019 Перевод организации\n'
 'Visa Classic 2842 87** **** 9012 -> Счет **3655   \n'
 '48150.39 USD',
 '19.11.2019 Перевод организации\n'
 'Maestro 7810 84** **** 5568 -> Счет **2869   \n'
 '30153.72 руб.',
 '13.11.2019 Перевод со счета на счет\n'
 'Счет 3861 14** **** 9794 -> Счет **8125   \n'
 '62814.53 руб.',
 '30.10.2019 Перевод с карты на счет\n'
 'Visa Gold 7756 67** **** 2839 -> Счет **9453   \n'
 '23036.03 руб.',
 '29.09.2019 Перевод со счета на счет\n'
 'Счет 3542 14** **** 9637 -> Счет **4961   \n'
 '45849.53 USD'] != ['07.12.2019 Перевод организации\n'
 'Visa Classic 2842 87** **** 9012 -> Счет **3655\n'
 '48150.39 USD']
