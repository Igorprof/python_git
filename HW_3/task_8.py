# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. 
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. 
# В конце следует вывести полученную матрицу.

SIZE_X = 5
SIZE_Y = 4
matrix = [[0 for _ in range(SIZE_Y)] for _ in range(SIZE_X)]

print(f'Введите матрицу {SIZE_X}x{SIZE_Y - 1}')

for i in range(SIZE_X):
    matrix[i][:-1] = map(lambda x: int(x), input().split())
    sum_ = 0
    for j in range(len(matrix[i]) - 1):
        sum_ += matrix[i][j]
    matrix[i][-1] = sum_

print('Результат: ')

print('\n'.join([' '.join(map(lambda x: str(x), line)) for line in matrix]))



