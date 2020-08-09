"""
 Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
 А также класс «Оргтехника», который будет базовым для классов-наследников
"""

class NumberExc(Exception):

    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f"На складе нет столько товара, есть {a}"

class Whouse:
    name: str
    max_volume: int = 1000
    staff: int
    equipm: dict

    def __init__(self, name, max_volume, staff, equipm):
        self.name = name
        self.max_volume = max_volume
        self.staff = staff
        self.equipm = equipm


    def whс(self, name, cnt):

        new_pr = self.equipm.setdefault(name) + cnt
        new_dict = {name: new_pr}
        self.equipm.update(new_dict)
        return self.equipm


    def whe(self, name, cnt):


        new_pr = self.equipm.setdefault(name) - cnt

        if new_pr >= 0:
            new_dict = {name: new_pr}
            self.equipm.update(new_dict)
            return self.equipm
        else:
            raise NumberExc(self.equipm.setdefault(name))


class OfficeEquipment:
    name: str
    yearprod: int = 2020
    color: str = 'white'
    weight: int = 3
    nameprod: str = 'HP'

    def __init__(self, name, yearprod, color, weight, nameprod):
        self.name = name
        self.yearprod = yearprod
        self.color = color
        self.weight = weight
        self.nameprod = nameprod

class Printer(OfficeEquipment):
    maxvolumesh: int
    sizesh: int

    def __init__(self, name, yearprod, color, weight, nameprod, maxvolumesh, sizesh):
        super().__init__(name, yearprod, color, weight, nameprod)
        self.maxvolumesh = maxvolumesh
        self.sizesh = sizesh

class Scaner(OfficeEquipment):
    sizesh: int

    def __init__(self, name, yearprod, color, weight, nameprod, sizesh):
        super().__init__(name, yearprod, color, weight, nameprod)
        self.sizesh = sizesh

class Xerox(OfficeEquipment):
    maxvolumesh: int


    def __init__(self, name, yearprod, color, weight, nameprod, maxvolumesh):
        super().__init__(name, yearprod, color, weight, nameprod)
        self.maxvolumesh = maxvolumesh


wh = Whouse(1, 1000, 4, {'print': 0, 'scaner': 0, 'xerox': 0})

printer1 = Printer('print', 2020, 'black', 10, 'HP', 1000, 'A4')
scaner1 = Scaner('scaner', 2020, 'black', 10, 'HP', 'A4')
xerox1 = Xerox('xerox', 2020, 'black', 10, 'HP', 1000)

print(printer1.name)

wh.whс('print', 40)
print(wh.equipm)

try:
    wh.whe('print', 60)
except NumberExc as num:
    print("Получается отрицательное значение, на скледе кол-во товара ", num.a)
print(wh.equipm)
