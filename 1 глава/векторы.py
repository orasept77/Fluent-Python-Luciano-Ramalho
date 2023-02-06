from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        # __str__ неявно вызывается методом print(), если нет str, вызывается repr.
        # REPR для отладки и протоколирования, STR для показа пользователям
        return f'Vector ({self.x} {self.y})'

    def __abs__(self):
        # hypot(x,y) = sqrt(x*x + y*y)
        return hypot(self.x, self.y)

    def __bool__(self):
        # false если x и y 0
        return bool(abs(self))

    def __add__(self, other):
        # сложение
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        # умножение
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(2, 5)
v2 = Vector(1, 3)
v3 = Vector(0, 0)

print(v1)
print(v2 + v1)
print(v1 * 5)
print(bool(v1))
print(bool(v3))
