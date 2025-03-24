from src.triangle import Triangle
import pytest


@pytest.mark.parametrize("side_a, side_b, side_c",
                         [(-3, 5, 10),
                          (3, -5, 10),
                          (3, 5, -10)],
                         ids=["first negative",
                              "second negative",
                              "third negative"]
                         )
def test_triangle_negative_sides(side_a, side_b, side_c):
    with pytest.raises(ValueError) as exc_info:
        t = Triangle(side_a, side_b, side_c)
    assert str(exc_info.value) == "Sides can't be less than 0"


@pytest.mark.parametrize("sides",
                         ["a > b + c",
                          "b > a + c",
                          "c > a + b"])
def test_triangle_with_disproportionate_sides(create_disproportionate_triangle, sides):
    side_a, side_b, side_c = create_disproportionate_triangle(sides=sides)
    with pytest.raises(ValueError) as exc_info:
        t = Triangle(side_a, side_b, side_c)
    assert str(exc_info.value) == f"Triangle with sides: {side_a}, {side_b}, {side_c} doesn't exist"


@pytest.mark.parametrize("sides",
                         ["integer",
                          "float"])
def test_rectangle_area(create_triangle, sides):
    side_a, side_b, side_c = create_triangle(sides=sides)
    t = Triangle(side_a, side_b, side_c)
    half_perimeter = (side_a + side_b + side_c) / 2
    area = (half_perimeter *
            (half_perimeter - side_a) *
            (half_perimeter - side_b) *
            (half_perimeter - side_c)) ** (1 / 2)
    assert t.area == area, f"Expected area {area}"


@pytest.mark.parametrize("sides",
                         ["integer",
                          "float"])
def test_rectangle_perimeter(create_triangle, sides):
    side_a, side_b, side_c = create_triangle(sides=sides)
    t = Triangle(side_a, side_b, side_c)
    assert t.perimeter == side_a + side_b + side_c, f"Expected perimeter {side_a + side_b + side_c}"
