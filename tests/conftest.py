import pytest


@pytest.fixture()
def create_rectangle():
    def _wrapper(sides):
        if sides == "integer":
            return 3, 5
        elif sides == "float":
            return 3.3, 5.5
        else:
            return ValueError("Sides must be integer or float")

    yield _wrapper


@pytest.fixture()
def create_square():
    def _wrapper(sides):
        if sides == "integer":
            return 3
        elif sides == "float":
            return 5.5
        else:
            return ValueError("Sides must be integer or float")

    yield _wrapper


@pytest.fixture()
def create_disproportionate_triangle():
    def _wrapper(sides):
        if sides == "a > b + c":
            return 10, 5, 1
        elif sides == "b > a + c":
            return 10, 17, 5
        elif sides == "c > a + b":
            return 3, 5, 10
        else:
            return ValueError("Sides must be integer or float")

    yield _wrapper


@pytest.fixture()
def create_triangle():
    def _wrapper(sides):
        if sides == "integer":
            return 3, 4, 5
        elif sides == "float":
            return 7.5, 8.5, 12.5
        else:
            return ValueError("Sides must be integer or float")

    yield _wrapper


@pytest.fixture()
def create_circle():
    def _wrapper(radius):
        if radius == "integer":
            return 7
        elif radius == "float":
            return 9.4
        else:
            return ValueError("Radius must be integer or float")

    yield _wrapper
