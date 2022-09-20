class Point:
    pointCount = 0

    def __init__(self, xVal, yVal):
        self.__x = xVal
        self.__y = yVal
        Point.pointCount += 1

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        self.__x = new_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        self.__y = new_y

    def __str__(self):
        return "(" + str(self.__x) + "," + str(self.__y) + ")"

    def distance(self, other):
        distx = (self.__x - other.__x) ** 2
        disty = (self.__y - other.__y) ** 2
        distancexy = (distx + disty) ** 0.5
        return distancexy

    def manhattan_distance(self, other):
        distx = abs(self.__x - other.__x)
        disty = abs(self.__y - other.__y)
        return distx + disty

    def cosine_distance(self, other):
        numerator = ((self.__x) * (other.__x)) + ((self.__y) * (other.__y))
        denominator = ((((self.__x) ** 2) + ((self.__y) ** 2))) ** 0.5 * (
            (((other.__x) ** 2) + ((other.__y) ** 2))) ** 0.5
        return numerator / denominator

    def method_overloading(self, a, b, c):
        print("three argument mehtod is called :", a, " ", b, " ", c)

    def method_overloading(self, a, b):
        print("two argument mehtod is called : ", a, " ", b)

    @staticmethod
    def displayPointCount():
        print("(" + str(Point.pointCount) + ")")


class PointInFirstQuadrant(Point):
    def __init__(self, x, y):
        if (x > 0 and y > 0):
            super().__init__(x, y)
        else:
            print('Invalid Co-ordinates!')

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        return repr('x = ' + str(self.x) + ', y = ' + str(self.y))


class PointInSecondQuadrant(Point):
    def __init__(self, x, y):
        if (x < 0 and y > 0):
            super().__init__(x, y)
        else:
            print('Invalid Co-ordinates!')

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        return repr('x = ' + str(self.x) + ', y = ' + str(self.y))


p1 = Point(1, 3)
p2 = Point(2, 5)
print("Distance : ", p1.distance(p2))
print()
print("Instance methods : ")
print("Manhattan Distance : ", p1.manhattan_distance(p2))
print("Cosine Distance : ", p1.cosine_distance(p2))
print()
print("Accessing private variables :   x =", p1.x)
print("Updating private variable : ")
print("Old y =", p1.y)
p1.y = 15
print("New y =", p1.y)
print("__str__ method gets called when the object is printed : ")
print(p1)
print("Method Overloading : ")
##print(p1.method_overloading(1, "abc", False))
##print(p1.method_overloading(2, "def"))
print("Method overloading is not possible in python, because everytime, the latest method will be called!")
print()
print("Inheritance : ")
p3 = PointInFirstQuadrant(7, 8)
print("Calling move method : ", p3.move(3, 3))
print()
p4 = PointInSecondQuadrant(-7, -8)
# print("Calling move method : ", p4.move(4, 4))
