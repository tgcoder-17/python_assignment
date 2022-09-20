import json
dict = {"name": "Tushar", "age": "21",
        "dob": "17-10-2001", "blood_group": "b+"}
dict1 = {"name": "harsh", "age": "22",
         "dob": "22-12-2001", "blood_group": "b+"}
list1 = []


def show_data():
    file = open('data.json', 'r')
    record = json.load(file)
    print(record)


def add_data(dictionary):
    list1.append(dictionary)
    file = open('data.json', 'w+')
    json.dump(list1, file)
    file.close()


add_data(dict)
add_data(dict1)
show_data()
