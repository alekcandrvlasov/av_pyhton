"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
my_list = []
i = int(input("Введите кол-во элементов списка >>> "))
while i > 0:
    my_list.append(input("Введите элемент списка >>> "))
    i -= 1
print(my_list)

new_my_list = []
new_len = len(my_list)

print(new_len)
i = 0
while i < new_len - 1:
    if i % 2 == 0:
        new_my_list.append(my_list[i + 1])
    else:
        new_my_list.append(my_list[i - 1])
    i += 1

new_my_list.append(my_list[new_len - 1]) if new_len % 2 != 0 else new_my_list.append(my_list[new_len - 2])

print(new_my_list)





