class Matrix:
    def __init__(self, matr):
        self.matr = matr.copy()
    def __str__(self):
        s_matr = '\n'.join([' '.join(str(row)[1:-1].split(', ')) for row in self.matr])
        return s_matr
    def __add__(self, other):
        m = [[0 for j in range(len(self.matr[0]))] for i in range(len(self.matr))]
        for i in range(len(self.matr)):
            for j in range(len(self.matr[0])):
                m[i][j] = self.matr[i][j] + other.matr[i][j]
        return Matrix(m)

matrix1 = Matrix([[1, 2, 3], [4, 4, 4], [7, 8, 5]])
matrix2 = Matrix([[3, 2, 1], [2, 3, 4], [1, 1, 2]])
print(matrix1)
print('---')
print(matrix2)
print('---')
print(matrix1 + matrix2)