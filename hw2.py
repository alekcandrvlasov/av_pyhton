"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
"""
from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def consamption(self):
        pass

class Coat(Clothes):

    def __init__(self, name: str,  color: str, v: float):
        self.name = name
        self.color = color
        self.v = v

    def consamption(self):
        return f'Расход ткани на 1 пальто  {self.v / 6.5 + 0.5 : .0f}'

    @property
    def short_name(self):
        return f'{self.name} {self.color}'

class Suit(Clothes):

    def __init__(self, h):
        self.h = h

    def consamption(self):
        return f'Расход ткани на 1 костюм  {2 * self.h + 0.3 : .0f}'

coat1 = Coat("tringle", "black", 100)
print(coat1.consamption())

suit1 = Suit(178)
print(suit1.consamption())

print("Общий расход ткани ", round(coat1.v / 6.5 + 0.5 + 2 * suit1.h + 0.3))

print(coat1.short_name)