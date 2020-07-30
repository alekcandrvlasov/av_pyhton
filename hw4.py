"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и
WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
сообщение о превышении скорости.
"""


class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print("Машина повернула ", direction)

    def show_speed(self, curspeed):
        print("Текущая скорость ам ", curspeed)

class TownCar(Car):
    limspeed: int

    def __init__(self, speed, color, name, is_police, limspeed):
        super().__init__(speed, color, name, is_police)
        self.limspeed = limspeed

    def show_speed(self, curspeed):
        print("Текущая скорость ам", curspeed)
        if curspeed > 60:
            print("Скорость превышена")

class SportCar(Car):
    maxspeed: int

    def __init__(self, speed, color, name, is_police, maxspeed):
        super().__init__(speed, color, name, is_police)
        self.maxspeed = maxspeed

class WorkCar(Car):
    maxspeed: int

    def __init__(self, speed, color, name, is_police, maxspeed):
        super().__init__(speed, color, name, is_police)
        self.maxspeed = maxspeed

    def show_speed(self, curspeed):
        print("Текущая скорость ам", curspeed)
        if curspeed > 40:
            print("Скорость превышена")

class PoliceCar(Car):
    maxspeed: int

    def __init__(self, speed, color, name, is_police, maxspeed):
        super().__init__(speed, color, name, is_police)
        self.maxspeed = maxspeed

auto1 = TownCar(100, 'red', 'Super', False, 30)
auto2 = WorkCar(80, 'red', 'Super', False, 100)
auto3 = SportCar(300, 'red', 'Super', False, 400)

auto1.go()
auto2.stop()
auto1.turn('На лево')
auto1.show_speed(200)
auto2.show_speed(200)

