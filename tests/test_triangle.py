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
        Triangle(side_a, side_b, side_c)
    assert exc_info.type is ValueError


@pytest.mark.parametrize("side_a, side_b, side_c",
                         [(10, 5, 1),
                          (10, 17, 5),
                          (3, 5, 10)],
                         ids=["a > b + c",
                              "b > a + c",
                              "c > a + b"])
def test_triangle_with_disproportionate_sides(side_a, side_b, side_c):
    with pytest.raises(ValueError) as exc_info:
        Triangle(side_a, side_b, side_c)
    assert exc_info.type is ValueError


@pytest.mark.parametrize("side_a, side_b, side_c, area",
                         [(3, 4, 5, 6),
                          (7.5, 8.5, 12.5, 31.110877820305873)],
                         ids=["integer",
                              "float"])
def test_rectangle_area(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    half_perimeter = (side_a + side_b + side_c) / 2
    assert t.area == area, f"Expected area {half_perimeter *
                                            (half_perimeter - side_a) *
                                            (half_perimeter - side_b) *
                                            (half_perimeter - side_c) ** (1 / 2)}"


@pytest.mark.parametrize("side_a, side_b, side_c, perimeter",
                         [(3, 4, 5, 12),
                          (7.5, 8.5, 12.5, 28.5)],
                         ids=["integer",
                              "float"])
def test_rectangle_perimeter(side_a, side_b, side_c, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.perimeter == perimeter, f"Expected perimeter {side_a + side_b + side_c}"
