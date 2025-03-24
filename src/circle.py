from src.figure import Figure
from math import pi


class Circle(Figure):

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius can't be less than 0")
        self.radius = radius

    @property
    def area(self):
        return pi * (self.radius ** 2)

    @property
    def perimeter(self):
        return 2 * pi * self.radius


c = Circle(3)
print(c.perimeter)
