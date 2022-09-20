from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        print("Shape Class")

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def circumference(self):
        pass


class Circle(Shape):
    def __init__(self):
        super().__init__()
        print("Circle Class")
        self.radius = int(input("Enter the radius: "))

    def area(self):
        print("Area of the Circle is %.2f." %
              ((22.0 / 7.0) * self.radius * self.radius))

    def circumference(self):
        print("Circumference of the Circle is %.2f." %
              (2 * (22.0 / 7.0) * self.radius))


class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        print("Rectangle Class")
        self.length = int(input("Enter the length: "))
        self.breadth = int(input("Enter the breadth: "))

    def area(self):
        print("Area of the Rectangle is %d." % (self.length * self.breadth))

    def circumference(self):
        print("Circumference of the Rectangle is %d." %
              (2 * (self.length + self.breadth)))


if __name__ == "__main__":
    print()
    c = Circle()
    c.area()
    c.circumference()
    print("\n")
    r = Rectangle()
    r.area()
    r.circumference()
