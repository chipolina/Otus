from math import pi
from typing import  Union

from src.Figure import Figure


class Circle(Figure):

    def __init__(self, radius: Union[float, int]):
        super().__init__(radius)
        self.name = "Circle"
        self.radius = radius

    @property
    def area(self) -> Union[float, int]:
        return round((pi * self.radius ** 2), 2)

    @property
    def perimeter(self) -> Union[float, int]:
        return round((2 * pi * self.radius), 2)
