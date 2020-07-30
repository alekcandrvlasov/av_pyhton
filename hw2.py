"""
Реализовать класс Road ( дорога), в котором определить атрибуты: l ength ( длина), width
(ширина).
"""

class Road:
    _l_enght: int
    _width: int

    def __init__(self, l_enght, width):
        self._width = width
        self._l_enght = l_enght

    def mass(self, massa, cm):
        print("Необходимая масса асфальта для дороги >>> ", massa * cm * self._width * self._l_enght)


road_1 = Road(10, 20)
road_1.mass(int(input("Введите массу асфальта >>> ")), int(input("Введите толщину асфальта >>> ")))

road_2 = Road(20, 20)
road_2.mass(int(input("Введите массу асфальта >>> ")), int(input("Введите толщину асфальта >>> ")))
