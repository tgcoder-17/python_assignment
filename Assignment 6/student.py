class Student:
    def __init__(self, name, rollno, address, gender, std, interests):
        self.name = name
        self.rollno = rollno
        self.address = address
        self.std = std
        self.gender = gender
        self.interests = interests

    def __str__(self):
        self.fileContent = 'Name : ' + self.name + '\n' + 'Roll no. :' + self.rollno + '\n' + 'Address : ' + self.address + \
            '\n' + 'Gender : ' + self.gender + '\n' + 'Standard :' + \
            self.std + '\n' + 'Interests : ' + self.interests
        return self.fileContent

    def saveAsFile(self):
        file = open(self.rollno + '-' + self.name + '.txt', 'w')
        file.write(self.fileContent)
        file.close()
