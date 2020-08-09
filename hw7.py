"""
Реализовать проект «Операции с комплексными числами»
"""
class Cnumber:

    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a + self.b * -1 ** 0.5}"

    def __add__(self, other):
        a, b = self.a + other.a, self.b + other.b
        return a + b * -1 ** 0.5

    def __mul__(self, other):
        a, b = self.a * other.a, self.b * other.b
        return a + b * -1 ** 0.5


k1 = Cnumber(1, 2)
k2 = Cnumber(1, 3)
print(k1)
print(k2)
print(k1 + k2)
print(k1 * k2)
