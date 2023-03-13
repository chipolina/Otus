from typing import Union

from src.Figure import Figure
from src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, a: Union[float, int]):
        super().__init__(a, a)
        self.name = "Square"
