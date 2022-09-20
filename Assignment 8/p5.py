class Demo:
    def __init__(self, a):
        self.a = a

    def __gt__(self, other):
        if(self.a > other.a):
            return True
        else:
            return False

    def __add__(self, other):
        return self.a + other.a

    def __sub__(self, other):
        return self.a - other.a

    def __str__(self):
        return str(self.a)


ob1 = Demo(20)
ob2 = Demo(40)
print("Ob1: ", ob1)
print("Ob2: ", ob2)
if(ob1 > ob2):
    print("ob1 is greater than ob2")
else:
    print("ob2 is greater than ob1")
print("ob1+ob2 = ", ob1+ob2)
print("ob1-ob2 = ", ob1-ob2)
