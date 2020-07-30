"""
Реализовать базовый класс Worker ( работник), в котором определить атрибуты: name,
surname, position ( должность), i ncome ( доход). Последний атрибут должен быть
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position ( должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника ( get_full_name) и
дохода с учетом премии ( get_total_income) . Проверить работу примера на реальных данных
(создать экземпляры класса Position , передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
"""


class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f"ФИО сотрудника >>>  {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Доход с учетом премии >>>  {self._income.get('wage') + self._income.get('bonus')}")


ivanov = Position("Иван", "Иванов", "Директор", 100000, 20000)

ivanov.get_full_name()
ivanov.get_total_income()
