from src.Figure import Figure
from math import sqrt
from typing import Union


class Triangle(Figure):

    def __init__(self, a: Union[float, int], b: Union[float, int], c: Union[float, int]):
        super().__init__(a, b, c)
        self.name = "Triangle"
        self.a = a
        self.b = b
        self.c = c
        self._check_figure()

    def _check_figure(self):
        """
        Проверяем возможность построить треугольник

        """
        if not (self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a):
            raise ValueError

    @property
    def area(self) -> float:
        p = self.perimeter
        return round((sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))), 2)

    @property
    def perimeter(self) -> float:
        return round(((self.a + self.b + self.c) / 2), 2)
