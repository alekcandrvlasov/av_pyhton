"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль
"""

class Zero(Exception):

    def __str__(self):
        return f"Деление на 0 невозможно"

try:
    a = int(input("Введите делимое "))
    b = int(input("Введите делитель "))

    if b == 0:
        raise Zero
    print(a / b)
except Zero:
    print("Деление на 0 невозможно")




