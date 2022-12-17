import model
import time

data = model.data
data_temp = data.copy()
print('Hello!')

while True:
    FLAG = False
    print('''\n1. Show all markets\n2. Find markets by city and State\n3. Find markets by zip\n0. Exit\n
To select the menu function, enter a number (1, 2, 3 or 0) and press Enter:\n''')
    print('What would you like to do? ')
    n = input()
    if n == '1':
        FLAG = True
        data_temp = model.show_all(data)
        for i, val in data_temp:
            print(f"{i}: {', '.join(val)}")

    elif n == '2':
        city = input('Please, enter the city: ').title()
        state = input('Please, enter the State: ').title()
        data_temp = model.search_markets_loc(data, city, state)
        if len(data_temp) > 0:
            FLAG = True
            for i, val in data_temp:
                print(f"{i}: {', '.join(val)}")
        else:
            print('Nothing was found. May be an error in the request.')

    elif n == '3':
        zip_code = input('Please, enter the zip code: ')
        data_temp = model.search_markets_zip(data, zip_code)
        if len(data_temp) > 0:
            FLAG = True
            for i, val in data_temp:
                print(f"{i}: {', '.join(val)}")
        else:
            print('Nothing was found. May be an error in the request.')

    elif n == '0':
        model.save_func()
        print('Bye!')
        break

    else:
        print('Input Error!')

    while FLAG is True:
        print('''\n1. Leave feedback\n2. Sort by Name\n3. Sort by city and State\n4. Sort by zip\n5. Delete\n
To select the menu function, enter a number (1, 2, 3, 4, 5 or other key to return to the main menu) and press Enter:''')
        print('What would you like to do? ')
        n = input()
        if n == '1':
            k = input('Enter the market id: ')
            if k.isdigit() and int(k) in range(len(data_temp)):
                feedback = input('Share your opinion: ')
                key = data_temp[int(k)][1]
                model.data[key]['Feedback'].append(feedback)
            else:
                print('Input Error!')
        elif n == '2':
            for i, val in sorted(data_temp, key=lambda x: x[1][0]):
                print(f"{i}: {', '.join(val)}")
        elif n == '3':
            for i, val in sorted(data_temp, key=lambda x: (x[1][-3], x[1][-2])):
                print(f"{i}: {', '.join(val)}")
        elif n == '4':
            for i, val in sorted(data_temp, key=lambda x: x[1][-1]):
                print(f"{i}: {', '.join(val)}")
        elif n == '5':
            while True:
                k = input('Enter id line to delete: ')
                if k.isdigit() and int(k) in range(len(data_temp)):
                    print('Deleted line:', data_temp[int(k)][1])
                    model.del_markets(data_temp[int(k)][1])
                    break
                else:
                    print('Input Error!')
        else:
            FLAG = False
        time.sleep(2)
    time.sleep(3)
