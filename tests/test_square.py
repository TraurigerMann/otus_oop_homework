from src.square import Square
import pytest


def test_square_negative_sides():
    with pytest.raises(ValueError) as exc_info:
        Square(-3)
    assert exc_info.type is ValueError


@pytest.mark.parametrize("side_a, area",
                         [(3, 9),
                          (7.5, 56.25)],
                         ids=["integer",
                              "float"])
def test_square_area(side_a, area):
    s = Square(side_a)
    assert s.area == area, f"Expected area {side_a * side_a}"


@pytest.mark.parametrize("side_a, perimeter",
                         [(3, 12),
                          (7.5, 30)],
                         ids=["integer",
                              "float"])
def test_square_perimeter(side_a, perimeter):
    s = Square(side_a)
    assert s.perimeter == perimeter, f"Expected perimeter {side_a * 4}"
