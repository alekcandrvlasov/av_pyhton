"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка
"""

with open("my_file.txt", "wt") as my_file:
    st = [input("Введите запись в файл >>> "), '\n']
    my_file.writelines(st)

with open("my_file.txt", "a") as my_file:
    while True:
        st = [input("Введите запись в файл >>> "), '\n']
        if not st[0]:
            print("Запись окончена")
            break
        else:
            my_file.writelines(st)
