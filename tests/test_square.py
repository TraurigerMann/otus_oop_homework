from src.square import Square
import pytest


def test_square_negative_sides():
    with pytest.raises(ValueError) as exc_info:
        s = Square(-3)
    assert str(exc_info.value) == "Sides can't be less than 0"


@pytest.mark.parametrize("sides",
                         ["integer",
                          "float"])
def test_square_area(create_square, sides):
    side_a = create_square(sides=sides)
    s = Square(side_a)
    assert s.area == side_a * side_a, f"Expected area {side_a * side_a}"


@pytest.mark.parametrize("sides",
                         ["integer",
                          "float"])
def test_square_perimeter(create_square, sides):
    side_a = create_square(sides=sides)
    s = Square(side_a)
    assert s.perimeter == side_a * 4, f"Expected perimeter {side_a * 4}"