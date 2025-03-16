from abc import ABC, abstractmethod


class Figure(ABC):

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError(f"Value {other_figure} -> {type(other_figure)} "
                             f"which is not a figure, need to pass figure argument")
        return self.area + other_figure.area
