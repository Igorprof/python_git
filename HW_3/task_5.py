# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. 

import random

SIZE = 100
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

i = 0
while (i < len(array)) and (array[i] >= 0):
    i += 1

if i < len(array):
    max_ = array[i]
    max_pos = i

    for i in range(max_pos + 1, len(array)):
        if (array[i] < 0) and (array[i] > max_):
            max_ = array[i]
            max_pos = i

    print(f'Максимальный отрицательный элемент находится на позиции {max_pos} и равен {max_}')
else:
    print('Отрицательных элементов в массиве нет')
