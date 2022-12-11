import csv

with open('./Data/Export.csv', 'r', encoding='utf-8') as file:
    data = {}
    for i in csv.DictReader(file):
        i.update({'Rating':[], 'Feedback':[]})
        data[(i['MarketName'], i['city'], i['State'], i['zip'])] = i


def show_all(dict_file):
    return dict_file


def search_markets_loc(dict_file, city, state):
    return list(filter(lambda x: (city, state) == x[1:3], dict_file))


def search_markets_zip(dict_file, zip_code):
    return list(filter(lambda x: zip_code in x[-1], dict_file))


def sort_markets(dict_file):
    return dict_file


def del_markets(dict_file):
    pass


def exit_func(dict_file):
    pass



