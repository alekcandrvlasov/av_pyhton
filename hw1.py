"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
"""

class Matrix:

    def __init__(self, matr: list):
        self.matr = matr

    def pr(self):
        for i in self.matr:
            for el in i:
                print(el, end=" ")
            print()
        print('\n')

    def __str__(self):
        return "{}\n{}\n{}".format(self.matr[0], self.matr[1], self.matr[2])

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.matr)):
            new_matrix1 = []
            for j in range(len(self.matr[i])):
                new_matrix1.append(int(self.matr[i][j]) + int(other.matr[i][j]))
            new_matrix.append(new_matrix1)
        return(new_matrix)



matr1 = Matrix([[1, 2, 3, 4, 5], [1, 2, 4, 4, 5], [1, 2, 3, 5, 5]])
matr2 = Matrix([[1, 2, 3, 4, 5], [1, 2, 4, 4, 5], [1, 2, 3, 5, 5]])
matr3 = Matrix([[4, 4, 4, 4, 4], [1, 2, 4, 4, 5], [1, 2, 3, 5, 5]])

matr1.pr()

print(matr1, '\n')

print(Matrix(matr1 + matr2), '\n')
print(Matrix(matr1 + matr3), '\n')

Matrix(matr1 + matr2).pr()
Matrix(matr1 + matr3).pr()