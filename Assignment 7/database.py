import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.con.execute("CREATE TABLE IF NOT EXISTS Student(Name varchar(255) NOT NULL, RollNo INTEGER NOT NULL, Address varchar(255) NOT NULL, Gender bit NOT NULL, Standard varchar(255) NOT NULL, Intrests varchar(255) NOT NULL)")
        self.con.commit()
        print("Connected to database")

    def insert(self, name, rollno, address, gender, std, intrests):
        self.con.execute(
            f"INSERT INTO Student (Name, RollNo, Address, Gender,Standard, Intrests) VALUES ('{name}', '{rollno}','{address}', '{gender}', '{std}', '{intrests}')")
        self.con.commit()

    def select(self):
        cur = self.con.execute(f"SELECT * FROM Student")
        student_list = cur.fetchall()
        return student_list
