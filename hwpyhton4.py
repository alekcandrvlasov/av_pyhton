# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

usnumber = input("Введите целое положительное число >>> ")

i = int(len(usnumber))-1

num1 = int(usnumber[i])
num2 = int(usnumber[i - 1])

while i >= 0:
    if num1 < num2:
        num1 = num2
        num2 = int(usnumber[i - 2])
    i -= 1

print("Самая большая цифра в числе >>> ", num1)