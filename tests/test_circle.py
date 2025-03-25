from src.circle import Circle
from math import pi
import pytest


def test_circle_negative_radius():
    with pytest.raises(ValueError) as exc_info:
        Circle(-10)
    assert exc_info.type is ValueError


@pytest.mark.parametrize("radius, area",
                         [(7, 153.93804),
                          (9.4, 277.59113)],
                         ids=["integer",
                              "float"])
def test_circle_area(radius, area):
    c = Circle(radius)
    assert c.area == area, f"Expected area {radius ** 2 * pi}"


@pytest.mark.parametrize("radius, perimeter",
                         [(7, 43.9823),
                          (9.4, 59.06194)],
                         ids=["integer",
                              "float"])
def test_circle_perimeter(radius, perimeter):
    c = Circle(radius)
    assert c.perimeter == perimeter, f"Expected perimeter {2 * pi * radius}"
