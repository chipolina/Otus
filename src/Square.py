from typing import Union

from src.Figure import Figure


class Square(Figure):
    def __init__(self, a: Union[float, int]):
        super().__init__(a)
        self.name = "Square"
        self.a = a

    @property
    def area(self) -> float:
        return self.a ** 2

    @property
    def perimeter(self) -> float:
        return self.a * 2
