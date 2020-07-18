"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов
"""


def my_func(arg1, arg2, arg3):
    """Функция возвращает сумму наибольших двух аргументов"""
    if arg3 == min(arg1, arg2, arg3):
        return arg1 + arg2
    elif arg2 == min(arg1, arg2, arg3):
        return arg1 + arg3
    elif arg1 == min(arg1, arg2, arg3):
        return arg2 + arg3


print(my_func(1, 2, 3))
