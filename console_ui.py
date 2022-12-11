import model
import time

data = model.data
data_temp = data.copy()
print('Hello!')

while True:
    flag = False
    print('''\n1. Show all markets\n2. Find markets by city and State\n3. Find markets by zip\n0. Exit\n
To select the menu function, enter a number (1, 2, 3 or 0) and press Enter:\n''')
    print('What would you like to do? ')
    n = input()
    if n == '1':
        flag = True
        for i in model.show_all(data):
            print(', '.join(i))

    elif n == '2':
        city = input('Please, enter the city: ').title()
        state = input('Please, enter the State: ').title()
        data_temp = model.search_markets_loc(data, city, state)
        if len(data_temp) > 0:
            flag = True
            for i in data_temp:
                print(', '.join(i))
        else:
            print('Nothing was found. May be an error in the request.')

    elif n == '3':
        zip_code = input('Please, enter the zip code: ')
        data_temp = model.search_markets_zip(data, zip_code)
        if len(data_temp) > 0:
            flag = True
            for i in data_temp:
                print(', '.join(i))
        else:
            print('Nothing was found. May be an error in the request.')

    elif n == '0':
        print('Bye!')
        break

    else:
        print('Input Error!')

    while flag is True:
        print('''\n1. Leave feedback\n2. Sort by Name\n3. Sort by city and State\n4. Sort by zip\n5. Delete\n
To select the menu function, enter a number (1, 2, 3 or other key to return to the main menu) and press Enter:''')
        print('What would you like to do? ')
        n = input()
        if n == '1':
            pass
        elif n == '2':
            for i in sorted(data_temp, key=lambda x: x[0]):
                print(', '.join(i))
        elif n == '3':
            for i in sorted(data_temp, key=lambda x: (x[-3], x[-2])):
                print(', '.join(i))
        elif n == '4':
            for i in sorted(data_temp, key=lambda x: x[-1]):
                print(', '.join(i))
        elif n == '5':
            pass
        else:
            flag = False
        time.sleep(2)
    time.sleep(3)

