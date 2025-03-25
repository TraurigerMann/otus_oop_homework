import pytest

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
