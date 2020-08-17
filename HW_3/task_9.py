# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE_X = 3
SIZE_Y = 3
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_Y)] for _ in range(SIZE_X)]

print(*matrix, sep='\n')

mins = matrix[0][:]

for line in matrix[1:]:
    for i, item in enumerate(line):
        if item < mins[i]:
            mins[i] = item

max_among_mins = mins[0]

for i in range(1, len(mins)):
    if mins[i] > max_among_mins:
        max_among_mins = mins[i]

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы равен {max_among_mins}')
    