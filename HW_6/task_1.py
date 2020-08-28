# Оценить задачу по памяти: собрать значения индексов четных элементов
# ОС: Win 10 64-bit; Python: 3.7.4 32-bit

import sys

def memory_demands(objects_list): # считает количество памяти, необходимое для хранения данного списка объектов(с учетом всех вложенностей)
    total_memory = 0

    def memory_calc(x):
        nonlocal total_memory
        total_memory += sys.getsizeof(x)
        if hasattr(x, '__iter__'):
            if hasattr(x, 'items'):
                for key, value in x.items():
                    memory_calc(key)
                    memory_calc(value)
            elif not isinstance(x, str):
                for item in x:
                    memory_calc(item)

    for obj in objects_list:
        memory_calc(obj)

    return total_memory


import random

def solution_1():
    SIZE = 100
    MIN_ITEM = 0
    MAX_ITEM = 1000
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    print(array)

    array_2 = [i for i in range(len(array)) if array[i] % 2 == 0]

    print(array_2)
   
    print(f'Решение #1. Потрачено памяти: {memory_demands(locals().values())}')

def solution_2():
    SIZE = 100
    MIN_ITEM = 0
    MAX_ITEM = 1000
    array = []
    array_2 = []
    for index in range(SIZE):
        item = random.randint(MIN_ITEM, MAX_ITEM)
        array.append(item)
        if item % 2 == 0:
            array_2.append(index)
        

    print(array)
    print(array_2)
   
    print(f'Решение #2. Потрачено памяти: {memory_demands(locals().values())}')

def solution_3():
    SIZE = 100
    MIN_ITEM = 0
    MAX_ITEM = 1000
    
    for index in range(SIZE):
        if random.randint(MIN_ITEM, MAX_ITEM) % 2 == 0:
            print(index, end = ' ')
    print()
    
   
    print(f'Решение #3. Потрачено памяти: {memory_demands(locals().values())}')

solution_1() # Потрачено памяти: 2708
solution_2() # Потрачено памяти: 2922
solution_3() # Потрачено памяти: 54


# При повторном запуске программ видим, что используемая каждой функцией(каждая функция - отдельный вариант решения задачи)
# память немного варьируется из-за случайных чисел, однако очевидно, что меньше всего памяти потребляет третий вариант решения
# (без использования списков, с выводом напрямую). При необходимости выводить оба списка (варианты 1 и 2) эффективней
# первый(с генераторами списков)
