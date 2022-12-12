import csv

with open('./Data/Export.csv', 'r', encoding='utf-8') as file:
    data = {}
    for i in csv.DictReader(file):
        i.update({'Rating': [], 'Feedback': []})
        data[(i['MarketName'], i['city'], i['State'], i['zip'])] = i


def show_all(dict_file):
    """The function return the dict object

    Args:
        dict_file (dict): The dict object

    Returns:
        dict: The dict object"""
    return dict_file


def search_markets_loc(dict_file, city, state):
    """The function filters the iterator object by the specified parameters

    Args:
        dict_file (dict): The dict object
        city (str): The first parameter.
        state (str): The second parameter.

    Returns:
        list: The filtered list object"""
    return list(filter(lambda x: (city, state) == x[1:3], dict_file))


def search_markets_zip(dict_file, zip_code):
    """The function filters the iterator object by the specified parameters

    Args:
        dict_file (dict): Dict object
        zip_code (str): The first parameter.

    Returns:
        list: The filtered list object"""
    return list(filter(lambda x: zip_code in x[-1], dict_file))


def sort_markets(dict_file):
    return dict_file


def del_markets(dict_file):
    return dict_file


def save_func(dict_file):
    return dict_file
