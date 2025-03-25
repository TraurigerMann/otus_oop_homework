from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle
from src.circle import Circle

import pytest


@pytest.mark.parametrize("first_figure_class, second_figure_class, first_figure_sides, second_figure_sides, area",
                         [(Rectangle, Triangle, (3, 5), (3, 4, 5), 15 + 6),
                          (Rectangle, Square, (2, 6), (3,), 12 + 9),
                          (Square, Circle, (4,), (5,), 16 + 78.53982)],
                         ids=["Rectangle + Triangle",
                              "Rectangle + Square",
                              "Square + Circle"])
def test_add_area(first_figure_class, second_figure_class, first_figure_sides, second_figure_sides, area):
    f1 = first_figure_class(*first_figure_sides)
    f2 = second_figure_class(*second_figure_sides)
    assert f1.add_area(f2) == area, f"Expected area {area}"
