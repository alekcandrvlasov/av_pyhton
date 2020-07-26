"""
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
"""

import io

with io.open("firm.txt", encoding='utf-8') as my_file:
    new_key = []
    new_type = []
    new_proceeds = []
    new_costs = []
    new_profit = []

    for el in my_file:
        new_key.append(el.split(' ')[0])
        new_type.append(el.split(' ')[1])
        new_proceeds.append(float(str(el.split(' ')[2])))
        new_costs.append(float(el.split(' ')[3].replace('\n', '')))


    for i in range(len(new_proceeds)):
        new_profit.append(new_proceeds[i] - new_costs[i])


    average_profit = sum(new_profit) / len(new_profit)
    new_dic = dict(zip(new_key, new_profit))
    new_dicap = {"average_profit": average_profit}

    new_str = [new_dic, new_dicap]
    print(new_str)

import json

with open("firm.json", "w") as my_json:
    json.dump(new_str, my_json)






