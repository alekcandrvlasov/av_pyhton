"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
"""
import time


class TrafficLight:
    __color: str

    def __init__(self, color):
        self.__color = color

    def running(self, tm):
        print(f"{self.__color}")
        time.sleep(tm)


tr1 = TrafficLight("Красный")
tr1.running(7)
tr2 = TrafficLight("Желтый")
tr2.running(2)
tr3 = TrafficLight("Зеленый")
tr3.running(2)