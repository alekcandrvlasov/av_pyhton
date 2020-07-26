"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
import io


with io.open("my_staff.txt", encoding='utf-8') as my_file:
    new_key = []
    new_atr = []
    for el in my_file:
        new_key.append(el.split(' ')[0])
        new_atr.append(float(el.split(' ')[1].replace('\n', '')))
    new_dic = dict(zip(new_key, new_atr))

    print("\nСписок сотрудников, кто имеет оклад менее 20 тыс >>> ")
    for key, value in new_dic.items():
        if value < 20000:
            print(key)

    print("\nСредняя величина дохода сотрудников >>> ")
    print(sum(new_dic.values()) / len(new_dic))






    #print("Список сотрудников, кто имеет оклад менее 20 тыс >>> ")

    #print("Количество строк в файле >>> ", len(st))
    #for n, l in enumerate(st, 1):
     #   print("Количество слов в строке ", n, " >>> ", len(l))




