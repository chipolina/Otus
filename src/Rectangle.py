from typing import  Union

from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, a: Union[float, int], b: Union[float, int]):
        super().__init__(a,b)
        self.name = "Rectangle"
        self.a = a
        self.b = b

    @property
    def area(self) -> float:
        return self.a * self.b

    @property
    def perimeter(self) -> float:
        return (self.a + self.b) * 2