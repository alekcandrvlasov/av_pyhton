"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел.
"""

class NumberExc(Exception):

    def __str__(self):
        return f"Введите число, а не строку"

l = []
a = 0

while a != '':
    a = input("Введите значение списка ")
    try:
        if a.isdigit():
            l.append(a)
        else:
            raise NumberExc
    except NumberExc:
        print("Введите число, а не строку")

print(l)


