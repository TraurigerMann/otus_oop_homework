from src.rectangle import Rectangle
import pytest


@pytest.mark.parametrize("side_a, side_b",
                         [(-3, 5),
                          (3, -5)],
                         ids=["first negative",
                              "second negative"])
def test_rectangle_negative_sides(side_a, side_b):
    with pytest.raises(ValueError) as exc_info:
        Rectangle(side_a, side_b)
    assert exc_info.type is ValueError


@pytest.mark.parametrize("side_a, side_b, area",
                         [(3, 5, 15),
                          (3.3, 5.5, 18.15)],
                         ids=["integer",
                              "float"])
def test_rectangle_area(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.area == area, f"Expected area {side_a * side_b}"


@pytest.mark.parametrize("side_a, side_b, perimeter",
                         [(3, 5, 16),
                          (3.3, 5.5, 17.6)],
                         ids=["integer",
                              "float"])
def test_rectangle_perimeter(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.perimeter == perimeter, f"Expected perimeter {(side_a + side_b) * 2}"

