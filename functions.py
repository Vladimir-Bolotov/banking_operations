import json
from datetime import datetime


def reading_operations():
    """
    Читает файл operations.json
    :return: список операций
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        operations = json.load(file)
        return operations


def executed_operations(operations):
    """
    Выбирает из списка операций все выполненые
    :param operations: список операций
    :return: список выполненых операций
    """
    executed_operations_list = []
    for operation in operations:
        if 'state' in operation:
            if operation and operation['state'] == 'EXECUTED':
                executed_operations_list.append(operation)
    return executed_operations_list


def sorted_operations(execute_operations):
    """
    Сортирует список выполненых операций по дате
    :param execute_operations:список выполненых операций
    :return: Отсортированый список выполненых операций
    """
    sort_operations = sorted(execute_operations, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'))
    return sort_operations


def get_last_operations(sort_operations):
    """
    Возвращает последние 5 операций
    :param sort_operations: Отсортированый список выполненых операций
    :return: Список последних 5 операций
    """

    return sort_operations[-1:-6:-1]


def account_number(card):
    """
    Разделяет платежную систему и номер счета
    :param card: платежная система и номер счета
    :return: кортеж: payment_system - платежную система, card_number - номер счета
    """
    card_number = []
    payment_system = []
    for symbol in card:
        if symbol.isdigit():
            card_number.append(symbol)
        else:
            payment_system.append(symbol)

    card_number = ''.join(card_number)
    payment_system = ''.join(payment_system)

    return payment_system, card_number


def preparing_printing(last_operations):
    """
    Подготавливает данные по операции к выводу на экран
    :param last_operations: данные по операции
    """
    print_operation = []
    for operation in last_operations:

        if 'description' in operation:
            description = operation['description']
        else:
            description = 'Неизвестно'

        if 'from' in operation:
            system, card = account_number(operation['from'])
            from_where = f"{system}{card[0:4]} {card[4:6]}** **** {card[-4:]}"

        else:
            from_where = 'Неизвестно'

        if 'to' in operation:
            bank_account, number = account_number(operation['to'])
            to = f"{bank_account}**{number[-4:]}"
        else:
            to = 'Неизвестно'
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']
        print_operation.append({
            'date': operation["date"],
            'description': description,
            'from': from_where,
            'to': to,
            'amount': amount,
            'currency': currency
        })

    return print_operation


def print_last_operations(print_operation):
    """
    Выводит список 5 последних операций на экран
    :param print_operation: список 5 последних операций
    """
    print(print_operation)
    for operation in print_operation:
        date = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f')
        print(f'{date: %d.%m.%Y} {operation["description"]}\n'
              f'{operation["from"]} -> {operation["to"]}\n'
              f'{operation["amount"]} {operation["currency"]}\n')
