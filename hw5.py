"""
Реализовать класс Stationery ( канцелярская принадлежность). Определить в нем атрибут t itle
(название) и метод draw ( отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
три дочерних класса Pen ( ручка), Pencil ( карандаш), Handle ( маркер). В каждом из классов
реализовать переопределение метода draw. Для каждого из классов метод должен выводить
уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра.
"""

class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    color: str

    def __init__(self, title, color):
        super().__init__(title)
        self.color = color

    def draw(self):
        print("Запуск отрисовки ручкой")

class Pencil(Stationery):
    color: str

    def __init__(self, title, color):
        super().__init__(title)
        self.color = color

    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    color: str

    def __init__(self, title, color):
        super().__init__(title)
        self.color = color

    def draw(self):
        print("Запуск отрисовки маркером")

tit1 = Pen('Ручка','Красный')
tit2 = Pencil('Карандаш','Красный')
tit3 = Handle('Маркер','Красный')

tit1.draw()
tit2.draw()
tit3.draw()