import pickle

def add_record():
    record = {}
    while True:
        print('[1]. Add Data')
        print('[2]. Exit')
        choice = int(input('Enter option : '))
        if choice == 1:
            key = input('Enter key : ')
            value = input('Enter value for ' + key + ' : ')
            record[key] = value
        elif choice == 2:
            break
        else:
            print('Invalid choice!')
    file = open('pickle2.dat', 'ab')
    pickle.dump(record, file)
    file.close()
    
def show_data():
    file = open('pickle2.dat', 'rb')
    while True:
        try:
            record = pickle.load(file)
            print(record)
        except:
            break
    file.close()


while True:
    print('1. Create/Update File')
    print('2. Show File')
    print('3. Exit')
    choice = int(input('Enter option : '))
    if choice == 1:
        add_record()
    elif choice == 2:
        show_data()
    elif choice == 3:
        break
    else:
        print('Invalid choice!')
