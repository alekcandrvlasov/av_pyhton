"""
Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка.
"""

class Cell:

    def __init__(self, cont: int):
        self.cont = cont

    def __add__(self, other):
        return self.cont + other.cont

    def __sub__(self, other):
        if self.cont - other.cont > 0:
            return self.cont - other.cont
        else:
            print("Ошибка, кол-во клеток отрицательно")

    def __mul__(self, other):
        return self.cont * other.cont

    def __truediv__(self, other):
        return self.cont // other.cont

    def make_order(self, r):
        for i in range(self.cont // r):
            for j in range(r):
                print('*', end='')
            print()
        for k in range(self.cont - r * (self.cont // r)):
            print('*', end='')




cell1 = Cell(4)
cell2 = Cell(10)

print(cell1 + cell2)
print(cell2 - cell1)
print(cell1 * cell2)
print(cell1 / cell2)

cell2.make_order(4)



