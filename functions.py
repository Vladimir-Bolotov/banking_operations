import json


def reading_operations():
    """
    Читает файл operations.json
    :return: список операций
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        operations = json.load(file)
        return operations


