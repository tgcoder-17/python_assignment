from tkinter import *
from student import Student


def saveData():
    address = addressText.get(1.0, 'end').strip()
    interests =[]
    if mathsInterest.get():
        interests.append("Math")
    if scienceInterest.get():
        interests.append('Science')
    else:
        interests.append('Not interested')

    student = Student(nameEntry.get(), rollEntry.get(), address,
                      gender.get(), stdSpinbox.get(), ", ".join(interests))
    print(student)
    student.saveAsFile()


mainWindow = Tk()
mainWindow.title("Student Application")
mainWindow.geometry("300x300")

Label(mainWindow, text="Name:").grid(row=0, column=0, sticky=W, pady=2)
nameEntry = Entry(mainWindow)
nameEntry.grid(row=0, column=1)

Label(mainWindow, text="Roll No:").grid(row=1, column=0, sticky=W, pady=2)
rollEntry = Entry(mainWindow)
rollEntry.grid(row=1, column=1)

Label(mainWindow, text="Gender:").grid(row=2, column=0, sticky=W, pady=2)
gender = StringVar()
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


mainWindow.mainloop()
