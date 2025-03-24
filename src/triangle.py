from src.figure import Figure


class Triangle(Figure):

    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Sides can't be less than 0")
        if side_a > side_b + side_c or side_b > side_a + side_c or side_c > side_a + side_b:
            raise ValueError(f"Triangle with sides: {side_a}, {side_b}, {side_c} doesn't exist")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self):
        half_perimeter = self.perimeter / 2
        return (half_perimeter *
                (half_perimeter - self.side_a) *
                (half_perimeter - self.side_b) *
                (half_perimeter - self.side_c)) ** (1 / 2)

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
