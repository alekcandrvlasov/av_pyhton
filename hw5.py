"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран
"""

with open("hw5.txt", "wt") as my_file:
    my_file.writelines("1 2 3 4 5 6 7 8 9")

with open("hw5.txt") as my_file:
    s = 0
    st = str(list(my_file))
    print(st)

    for i in range(2, len(list(st))-2):
        if st[i] != ' ':
            s = s + int(st[i])
        
    print("Сумма чсисел в файле >>> ", s)




