import csv

with open('./Data/Export.csv', 'r', encoding='utf-8') as file:
    data = {}
    for i in csv.DictReader(file):
        i.update({'Rating': [], 'Feedback': []})

        data[(i['MarketName'], i['city'], i['State'], i['zip'])] = i
    fieldnames = i.keys()

def show_all(dict_file):
    """The function return the dict object

    Args:
        dict_file (dict): The dict object

    Returns:
        dict: The dict object"""
    return list(enumerate(dict_file, 1))


def search_markets_loc(dict_file, city, state):
    """The function filters the iterator object by the specified parameters

    Args:
        dict_file (dict): The dict object
        city (str): The first parameter.
        state (str): The second parameter.

    Returns:
        list: The filtered list object"""
    return [(i, val) for i, val in enumerate(filter(lambda x: (city, state) == x[1:3], dict_file), 0)]


def search_markets_zip(dict_file, zip_code):
    """The function filters the iterator object by the specified parameters

    Args:
        dict_file (dict): Dict object
        zip_code (str): The first parameter.

    Returns:
        list: The filtered list object"""
    return [(i, val) for i, val in enumerate(filter(lambda x: zip_code in x[-1], dict_file), 0)]


def sort_markets(dict_file):
    return dict_file


def del_markets(key):
    global data
    del data[key]


def save_func():
    with open('./Data/Export.csv', 'w', encoding='utf-8') as file_update:
        writer = csv.DictWriter(file_update, fieldnames=fieldnames)
        writer.writeheader()
        for i in data:
            writer.writerow(data[i])


