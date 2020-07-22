"""
Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
"""

my_list = [1, 2, 3, 45, 3, 8, 56]


print(my_list)

new_list = []

for i in range(len(my_list) - 1):
    if my_list[i + 1] > my_list[i]:
        new_list.append(my_list[i + 1])

print(new_list)

new_list2 = [my_list[i + 1] for i in range(len(my_list) - 1) if my_list[i + 1] > my_list[i]]

print(new_list2)