import pickle
dict = {"name": "Tushar", "age": "21",
        "dob": "17-10-2001", "blood_group": "b+"}
dict1 = {"name": "harsh", "age": "22",
         "dob": "22-11-2001", "blood_group": "b+"}


def add_record(dictionary):
    file = open('pickle1.dat', 'ab')
    pickle.dump(dictionary, file)
    file.close()


def show_data():
    file = open('pickle1.dat', 'rb')
    while True:
        try:
            record = pickle.load(file)
            print(record)
        except:
            break
    file.close()


add_record(dict)
add_record(dict1)
show_data()
