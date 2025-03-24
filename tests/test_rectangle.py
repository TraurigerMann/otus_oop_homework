from src.rectangle import Rectangle
from src.square import Square
import pytest


@pytest.mark.parametrize("side_a, side_b",
                         [(-3, 5),
                          (3, -5)],
                         ids=["first negative",
                              "second negative"])
def test_rectangle_negative_sides(side_a, side_b):
    with pytest.raises(ValueError) as exc_info:
        r = Rectangle(side_a, side_b)
    assert str(exc_info.value) == "Sides can't be less than 0"


@pytest.mark.parametrize("sides",
                         ["integer",
                          "float"])
def test_rectangle_area(create_rectangle, sides):
    side_a, side_b = create_rectangle(sides=sides)
    r = Rectangle(side_a, side_b)
    assert r.area == side_a * side_b, f"Expected area {side_a * side_b}"


@pytest.mark.parametrize("sides",
                         ["integer",
                          "float"])
def test_rectangle_perimeter(create_rectangle, sides):
    side_a, side_b = create_rectangle(sides=sides)
    r = Rectangle(side_a, side_b)
    assert r.perimeter == (side_a + side_b) * 2, f"Expected perimeter {(side_a + side_b) * 2}"


@pytest.mark.parametrize("sides",
                         ["integer",
                          "float"])
def test_add_area(create_rectangle, sides):
    side_a, side_b = create_rectangle(sides=sides)
    r = Rectangle(side_a, side_b)
    s = Square(side_a)
    assert r.add_area(s) == side_a * side_b + side_a ** 2, f"Expected area {side_a * side_b + side_a ** 2}"
