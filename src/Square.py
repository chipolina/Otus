from typing import Union

from src.Figure import Figure
from src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, a: Union[float, int], b=None):
        super().__init__(a, b)
        self.name = "Square"
        self.a = a

    @property
    def area(self) -> Union[float, int]:
        return self.a ** 2

    @property
    def perimeter(self) -> Union[float, int]:
        return self.a * 2
