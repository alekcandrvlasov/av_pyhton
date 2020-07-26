"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

import io

with open("numbers.txt") as my_file:

    new_key = []
    new_atr = []
    for el in my_file:
        new_key.append(el.split(' ')[0])
        new_atr.append(int(el.split(' ')[2].replace('\n', '')))
    rus = ['один', 'два', 'три', 'четыре']
    new_dic = dict(zip(rus, new_atr))
    print(new_dic)

with io.open("numbers2.txt", "wt", encoding='utf-8') as my_file2:
    for el in str(new_dic.items()):
        my_file2.writelines(el)
        




