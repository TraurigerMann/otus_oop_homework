from src.circle import Circle
from math import pi
import pytest


def test_circle_negative_radius():
    with pytest.raises(ValueError) as exc_info:
        c = Circle(-10)
    assert str(exc_info.value) == "Radius can't be less than 0"


@pytest.mark.parametrize("radius",
                         ["integer",
                          "float"])
def test_circle_area(create_circle, radius):
    radius = create_circle(radius=radius)
    c = Circle(radius)
    assert c.area == radius ** 2 * pi, f"Expected area {radius ** 2 * pi}"


@pytest.mark.parametrize("radius",
                         ["integer",
                          "float"])
def test_circle_perimeter(create_circle, radius):
    radius = create_circle(radius=radius)
    c = Circle(radius)
    assert c.perimeter == 2 * pi * radius, f"Expected perimeter {2 * pi * radius}"
