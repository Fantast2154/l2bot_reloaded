from __future__ import annotations

import math


class Vector2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __mul__(self, other: float) -> Vector2:
        return Vector2(self.x * other, self.y * other)

    def __add__(self, other: Vector2) -> Vector2:
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2) -> Vector2:
        return Vector2(self.x - other.x, self.y - other.y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def dot(self, other: Vector2) -> float:
        return self.x * other.x + self.y * other.y

    def normalized(self) -> Vector2:
        length = self.get_length()
        x_normed = self.x / length
        y_normed = self.y / length
        return Vector2(x_normed, y_normed)


class Vector2i:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __mul__(self, other: int) -> Vector2i:
        return Vector2i(self.x * other, self.y * other)

    def __add__(self, other: Vector2i) -> Vector2i:
        return Vector2i(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2i) -> Vector2i:
        return Vector2i(self.x - other.x, self.y - other.y)

    def __bool__(self):
        return self.get_length() > 0

    def get_length(self) -> int:
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

    def dot(self, other: Vector2) -> int:
        return int(self.x * other.x + self.y * other.y)

    def normalized(self) -> Vector2i:
        length = self.get_length()

        if length == 0:
            raise Exception('Cant normalize zero-length vector. Poshel naher, kozel ebaniy')

        x_normed = int(self.x / length)
        y_normed = int(self.y / length)
        return Vector2i(x_normed, y_normed)
