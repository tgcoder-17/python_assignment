import json


def show_data():
    file = open('data1.json', 'r')
    record = json.load(file)
    print(record)
    file.close()


def add_data():
    dictionary = {}
    while True:
        print('1. Add Data')
        print('2. Exit')
        choice = int(input('Enter option : '))
        if choice == 1:
            key = input('Enter key : ')
            value = input('Enter value for ' + key + ' : ')
            dictionary[key] = value
        elif choice == 2:
            break
        else:
            print('Invalid choice!')

    print('Final Data : ', dictionary)
    print('1. Create file')
    print('2. Update file')
    print('3. Exit')
    choice = int(input('Enter option : '))
    file = None
    list = []
    if choice == 1:
        file = open('data1.json', 'w+')
        print('Creating new file...')
    elif choice == 2:
        file = open('data1.json', 'r')
        list = json.load(file)
        file.close()
        file = open('data1.json', 'w+')
        print('Updating file...')
    elif choice == 3:
        return
    else:
        print('Invalid choice!')
    list.append(dictionary)
    json.dump(list, file)
    file.close()


while True:
    print('1. Create/Update JSON File')
    print('2. Show JSON File')
    print('3. Exit')
    choice = int(input('Enter option : '))
    if choice == 1:
        add_data()
    elif choice == 2:
        show_data()
    elif choice == 3:
        break
    else:
        print('Invalid choice!')
