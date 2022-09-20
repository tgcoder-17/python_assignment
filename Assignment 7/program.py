from turtle import width
from database import Database
from functools import partial
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import Treeview

db = Database("SQLLite")


def saveData():
    address = addressText.get(1.0, 'end').strip()
    interests = []
    if mathsInterest.get():
        interests.append("Math")
    if scienceInterest.get():
        interests.append('Science')
    else:
        interests.append('Not interested')

    db.insert(nameEntry.get(), rollEntry.get(), address,
              gender.get(), stdSpinbox.get(), ", ".join(interests))
    gender.set("Male")
    mathsInterest.set(False)
    scienceInterest.set(False)
    getStudents(tree)


def getStudents(trElem):
    students = db.select()
    for item in trElem.get_children():
        trElem.delete(item)
    for student in students:
        trElem.insert('', 'end', text="1", values=student)


onSubmit = partial(saveData)

mainWindow = Tk()
mainWindow.title("Student Application")
mainWindow.geometry("600x500")

Label(mainWindow, text="Name:").grid(row=0, column=0, sticky=W, pady=2)
nameEntry = Entry(mainWindow)
nameEntry.grid(row=0, column=1)

Label(mainWindow, text="Roll No:").grid(row=1, column=0, sticky=W, pady=2)
rollEntry = Entry(mainWindow)
rollEntry.grid(row=1, column=1)

Label(mainWindow, text="Gender:").grid(row=2, column=0, sticky=W, pady=2)
gender = StringVar()
gender.set("Male")

maleRadio = Radiobutton(mainWindow, text="Male", value="Male", variable=gender)
maleRadio.grid(row=2, column=1)
femaleRadio = Radiobutton(mainWindow, text="Female",
                          value="Female", variable=gender)
femaleRadio.grid(row=3, column=1)

Label(mainWindow, text="Address:").grid(row=4, column=0, sticky=W, pady=2)
addressText = Text(mainWindow,  height=3, width=15)
addressText.grid(row=4, column=1)

Label(mainWindow, text="Standard:").grid(row=5, column=0, sticky=W, pady=2)
stdSpinbox = Spinbox(mainWindow, from_=1, to=10)
stdSpinbox.grid(row=5, column=1)

Label(mainWindow, text="Interested in:").grid(
    row=6, column=0, sticky=W, pady=2)
mathsInterest = BooleanVar()
mathsInterest.set(False)
mathCheckbox = Checkbutton(mainWindow, text="Maths", variable=mathsInterest)
mathCheckbox.grid(row=6, column=1)

scienceInterest = BooleanVar()
scienceInterest.set(False)
scienceCheckbox = Checkbutton(
    mainWindow, text="Science", variable=scienceInterest)
scienceCheckbox.grid(row=7, column=1)


Button(mainWindow, text="Submit", command=saveData).grid(
    row=9, column=1, pady=10)

Label(mainWindow, text="Student Data").grid(row=11, pady=10)

tree = Treeview(mainWindow, column=("Name", "RollNo", "Address", "Gender",
                "Standard", "Intrests"), show='headings', height=5)
tree.grid(row=13, columnspan=20)
tree.column("# 1", anchor=CENTER, width=100)
tree.heading("# 1", text="Name")
tree.column("# 2", anchor=CENTER, width=100)
tree.heading("# 2", text="RollNo")
tree.column("# 3", anchor=CENTER, width=100)
tree.heading("# 3", text="Address")
tree.column("# 4", anchor=CENTER, width=100)
tree.heading("# 4", text="Gender")
tree.column("# 5", anchor=CENTER, width=100)
tree.heading("# 5", text="Standard")
tree.column("# 6", anchor=CENTER, width=100)
tree.heading("# 6", text="Interests")
getStudents(tree)

mainWindow.mainloop()
