# Classes
print("-" * 20 + "\n Classes \n" + "-" * 20)


class Point:
    default_color = "red"  # class level attribute

    # constructor
    # any method with __ is a magic method and they are called by Python interpreter
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):  # class method, cls refers to class and not instance here
        return cls(0, 0)

    # magic method
    def __str__(self):
        return f"({self.x}, {self.y})"

    # returns boolean
    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y

    def __gt__(self, other: object) -> bool:
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(2, 3)
print(type(point))
print(isinstance(point, Point))
print(point.x, point.y)
point.draw()

another = Point.zero()
another.draw()

# Class and instance attributes
print("-" * 20 + "\n Class and instance attributes \n" + "-" * 20)
point.z = 10  # instance attributes
print(point.default_color)
print(Point.default_color)


# Magic methods
print("-" * 20 + "\n Magic methods \n" + "-" * 20)
print(another.__str__())
print(str(another))  # same as above
print(another)

# Compare objects
print("-" * 20 + "\n Compare objects \n" + "-" * 20)
pointA = Point(1, 2)
pointB = Point(3, 4)
print(pointA == pointB)  # returns false without the magic method __eq__
print(pointA < pointB)  # returns error withou the magic method __gt__

# Arithmetic operations
print("-" * 20 + "\n Arithmetic operations \n" + "-" * 20)
combined = pointA + pointB
combined.draw()


# Custom Containers
print("-" * 20 + "\n Custom Containers \n" + "-" * 20)
