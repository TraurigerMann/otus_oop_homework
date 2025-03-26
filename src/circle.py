from src.figure import Figure
from math import pi


class Circle(Figure):

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius can't be less than 0")
        self.radius = radius

    @property
    def area(self):
        return round(pi * (self.radius ** 2), 5)

    @property
    def perimeter(self):
        return round(2 * pi * self.radius, 5)


c = Circle(5)
print(c.area)



