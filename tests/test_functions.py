import pytest

import functions


@pytest.fixture
def list_operation():
    return [
        {
            "id": 200634844,
            "state": "CANCELED",
            "date": "2018-02-13T04:43:11.374324",
            "operationAmount": {
                "amount": "42210.20",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 33355011456314142963",
            "to": "Счет 45735917297559088682"
        },
        {
            "id": 879660146,
            "state": "EXECUTED",
            "date": "2019-07-22T07:42:32.953324",
            "operationAmount": {
                "amount": "92130.50",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 19628854383215954147",
            "to": "Счет 90887717138446397473"
        },
        {
            "id": 893507143,
            "state": "CANCELED",
            "date": "2018-02-03T07:16:28.366141",
            "operationAmount": {
                "amount": "90297.21",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 37653295304860108767"
        }, {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 596171168,
            "state": "CANCELED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {
                "amount": "79931.03",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215"
        },
        {
            "id": 716496732,
            "state": "CANCELED",
            "date": "2018-04-04T17:33:34.701093",
            "operationAmount": {
                "amount": "40701.91",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Gold 5999414228426353",
            "to": "Счет 72731966109147704472"
        },

    ]


def test_executed_operations(list_operation):
    assert functions.executed_operations(list_operation) == [{'date': '2019-07-22T07:42:32.953324',
                                                              'description': 'Перевод организации',
                                                              'from': 'Счет 19628854383215954147',
                                                              'id': 879660146,
                                                              'operationAmount': {'amount': '92130.50',
                                                                                  'currency': {'code': 'USD',
                                                                                               'name': 'USD'}},
                                                              'state': 'EXECUTED',
                                                              'to': 'Счет 90887717138446397473'},
                                                             {'date': '2018-08-19T04:27:37.904916',
                                                              'description': 'Перевод с карты на карту',
                                                              'from': 'Visa Classic 6831982476737658',
                                                              'id': 895315941,
                                                              'operationAmount': {'amount': '56883.54',
                                                                                  'currency': {'code': 'USD',
                                                                                               'name': 'USD'}},
                                                              'state': 'EXECUTED',
                                                              'to': 'Visa Platinum 8990922113665229'}]


def test_sorted_operations(list_operation):
    assert functions.sorted_operations(list_operation) == [{'date': '2018-02-03T07:16:28.366141',
                                                            'description': 'Открытие вклада',
                                                            'id': 893507143,
                                                            'operationAmount': {'amount': '90297.21',
                                                                                'currency': {'code': 'RUB',
                                                                                             'name': 'руб.'}},
                                                            'state': 'CANCELED',
                                                            'to': 'Счет 37653295304860108767'},
                                                           {'date': '2018-02-13T04:43:11.374324',
                                                            'description': 'Перевод организации',
                                                            'from': 'Счет 33355011456314142963',
                                                            'id': 200634844,
                                                            'operationAmount': {'amount': '42210.20',
                                                                                'currency': {'code': 'RUB',
                                                                                             'name': 'руб.'}},
                                                            'state': 'CANCELED',
                                                            'to': 'Счет 45735917297559088682'},
                                                           {'date': '2018-04-04T17:33:34.701093',
                                                            'description': 'Перевод организации',
                                                            'from': 'Visa Gold 5999414228426353',
                                                            'id': 716496732,
                                                            'operationAmount': {'amount': '40701.91',
                                                                                'currency': {'code': 'USD',
                                                                                             'name': 'USD'}},
                                                            'state': 'CANCELED',
                                                            'to': 'Счет 72731966109147704472'},
                                                           {'date': '2018-07-11T02:26:18.671407',
                                                            'description': 'Открытие вклада',
                                                            'id': 596171168,
                                                            'operationAmount': {'amount': '79931.03',
                                                                                'currency': {'code': 'RUB',
                                                                                             'name': 'руб.'}},
                                                            'state': 'CANCELED',
                                                            'to': 'Счет 72082042523231456215'},
                                                           {'date': '2018-08-19T04:27:37.904916',
                                                            'description': 'Перевод с карты на карту',
                                                            'from': 'Visa Classic 6831982476737658',
                                                            'id': 895315941,
                                                            'operationAmount': {'amount': '56883.54',
                                                                                'currency': {'code': 'USD',
                                                                                             'name': 'USD'}},
                                                            'state': 'EXECUTED',
                                                            'to': 'Visa Platinum 8990922113665229'},
                                                           {'date': '2019-07-22T07:42:32.953324',
                                                            'description': 'Перевод организации',
                                                            'from': 'Счет 19628854383215954147',
                                                            'id': 879660146,
                                                            'operationAmount': {'amount': '92130.50',
                                                                                'currency': {'code': 'USD',
                                                                                             'name': 'USD'}},
                                                            'state': 'EXECUTED',
                                                            'to': 'Счет 90887717138446397473'}]


def test_get_last_operations(list_operation):
    assert functions.get_last_operations(list_operation) == [{'date': '2018-04-04T17:33:34.701093',
                                                              'description': 'Перевод организации',
                                                              'from': 'Visa Gold 5999414228426353',
                                                              'id': 716496732,
                                                              'operationAmount': {'amount': '40701.91',
                                                                                  'currency': {'code': 'USD',
                                                                                               'name': 'USD'}},
                                                              'state': 'CANCELED',
                                                              'to': 'Счет 72731966109147704472'},
                                                             {'date': '2018-07-11T02:26:18.671407',
                                                              'description': 'Открытие вклада',
                                                              'id': 596171168,
                                                              'operationAmount': {'amount': '79931.03',
                                                                                  'currency': {'code': 'RUB',
                                                                                               'name': 'руб.'}},
                                                              'state': 'CANCELED',
                                                              'to': 'Счет 72082042523231456215'},
                                                             {'date': '2018-08-19T04:27:37.904916',
                                                              'description': 'Перевод с карты на карту',
                                                              'from': 'Visa Classic 6831982476737658',
                                                              'id': 895315941,
                                                              'operationAmount': {'amount': '56883.54',
                                                                                  'currency': {'code': 'USD',
                                                                                               'name': 'USD'}},
                                                              'state': 'EXECUTED',
                                                              'to': 'Visa Platinum 8990922113665229'},
                                                             {'date': '2018-02-03T07:16:28.366141',
                                                              'description': 'Открытие вклада',
                                                              'id': 893507143,
                                                              'operationAmount': {'amount': '90297.21',
                                                                                  'currency': {'code': 'RUB',
                                                                                               'name': 'руб.'}},
                                                              'state': 'CANCELED',
                                                              'to': 'Счет 37653295304860108767'},
                                                             {'date': '2019-07-22T07:42:32.953324',
                                                              'description': 'Перевод организации',
                                                              'from': 'Счет 19628854383215954147',
                                                              'id': 879660146,
                                                              'operationAmount': {'amount': '92130.50',
                                                                                  'currency': {'code': 'USD',
                                                                                               'name': 'USD'}},
                                                              'state': 'EXECUTED',
                                                              'to': 'Счет 90887717138446397473'}]


def test_account_number():
    assert functions.account_number('Visa Classic 2842878893689012') == ('Visa Classic ', '2842878893689012')
    assert functions.account_number('2842878893689012') == ('', '2842878893689012')
    assert functions.account_number('Счет 35') == ('Счет ', '35')


def test_preparing_printing(list_operation):
    assert functions.preparing_printing(list_operation) == [{'amount': '42210.20',
                                                             'currency': 'руб.',
                                                             'date': '2018-02-13T04:43:11.374324',
                                                             'description': 'Перевод организации',
                                                             'from': 'Счет 3335 50** **** 2963',
                                                             'to': 'Счет **8682'},
                                                            {'amount': '92130.50',
                                                             'currency': 'USD',
                                                             'date': '2019-07-22T07:42:32.953324',
                                                             'description': 'Перевод организации',
                                                             'from': 'Счет 1962 88** **** 4147',
                                                             'to': 'Счет **7473'},
                                                            {'amount': '90297.21',
                                                             'currency': 'руб.',
                                                             'date': '2018-02-03T07:16:28.366141',
                                                             'description': 'Открытие вклада',
                                                             'from': 'Неизвестно',
                                                             'to': 'Счет **8767'},
                                                            {'amount': '56883.54',
                                                             'currency': 'USD',
                                                             'date': '2018-08-19T04:27:37.904916',
                                                             'description': 'Перевод с карты на карту',
                                                             'from': 'Visa Classic 6831 98** **** 7658',
                                                             'to': 'Visa Platinum **5229'},
                                                            {'amount': '79931.03',
                                                             'currency': 'руб.',
                                                             'date': '2018-07-11T02:26:18.671407',
                                                             'description': 'Открытие вклада',
                                                             'from': 'Неизвестно',
                                                             'to': 'Счет **6215'},
                                                            {'amount': '40701.91',
                                                             'currency': 'USD',
                                                             'date': '2018-04-04T17:33:34.701093',
                                                             'description': 'Перевод организации',
                                                             'from': 'Visa Gold 5999 41** **** 6353',
                                                             'to': 'Счет **4472'}]
