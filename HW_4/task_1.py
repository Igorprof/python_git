# Задача для анализа: Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… 

import sys
import timeit
import cProfile

sys.setrecursionlimit(3500)

# 1 - решение рекурсией
def calc_range(cur, n):
    if (n == 1):
        return cur
    return cur + calc_range(cur * (-0.5), n - 1)

print(timeit.timeit('calc_range(1, 5)', number=100, globals=globals()))  # N = 5 t = 0.00014220000000000899
print(timeit.timeit('calc_range(1, 25)', number=100, globals=globals()))  # N = 25 t = 0.000902900000000012
print(timeit.timeit('calc_range(1, 125)', number=100, globals=globals()))  # N = 125 t = 0.007338499999999998
print(timeit.timeit('calc_range(1, 625)', number=100, globals=globals())) # N = 625 t = 0.0395045
print(timeit.timeit('calc_range(1, 3125)', number=100, globals=globals())) # N = 3125 t = 0.28707360000000004


cProfile.run('calc_range(1, 5)')
# 5/1    0.000    0.000    0.000    0.000 task_1.py:8(calc_range)
cProfile.run('calc_range(1, 25)')
# 25/1    0.000    0.000    0.000    0.000 task_1.py:8(calc_range)
cProfile.run('calc_range(1, 125)')
# 125/1    0.000    0.000    0.000    0.000 task_1.py:8(calc_range)
cProfile.run('calc_range(1, 625)')
# 625/1    0.001    0.000    0.001    0.001 task_1.py:8(calc_range)
cProfile.run('calc_range(1, 3125)')
# 3125/1    0.003    0.000    0.003    0.003 1.py:10(calc_range)
print('='*20)

# 2 - сохрание членов в список и вложенный цикл для подсчета очередного члена
def calc_range_mem(n):
    range_members = []
    for i in range(n):
        cur = 1
        q = i
        while (q):
            cur *= (-1/2)
            q -= 1
        range_members.append(cur)
    sum_ = 0
    for item in range_members:
        sum_ += item
    return sum_

print(timeit.timeit('calc_range_mem(5)', number=100, globals=globals()))  # N = 5 t = 0.0006058000000000174
print(timeit.timeit('calc_range_mem(25)', number=100, globals=globals()))  # N = 25 t = 0.012894899999999987
print(timeit.timeit('calc_range_mem(125)', number=100, globals=globals()))  # N = 125 t = 0.2844796
print(timeit.timeit('calc_range_mem(625)', number=100, globals=globals())) # N = 625 t = 5.3824744
# print(timeit.timeit('calc_range_mem(3125)', number=100, globals=globals())) # N = 3125 t = 144.6175705

cProfile.run('calc_range_mem(5)')
# 1    0.000    0.000    0.000    0.000 task_1.py:35(calc_range_mem)
# 5    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('calc_range_mem(25)')
# 1    0.000    0.000    0.000    0.000 task_1.py:35(calc_range_mem)
# 25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('calc_range_mem(125)')
# 1    0.003    0.003    0.003    0.003 task_1.py:35(calc_range_mem)
# 125    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
cProfile.run('calc_range_mem(625)')
# 1    0.056    0.056    0.057    0.057 task_1.py:35(calc_range_mem)
# 625    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('calc_range_loop(3125)')
print('='*20)

# 3 - решение циклом
def calc_range_loop(n):
    cur = 1
    sum_ = cur
    for _ in range(n - 1):
        cur *= (-0.5)
        sum_ += cur
    return sum_

print(timeit.timeit('calc_range_loop(5)', number=100, globals=globals()))  # N = 5 t = 0.00031770000000003185
print(timeit.timeit('calc_range_loop(25)', number=100, globals=globals()))  # N = 25 t = 0.0008349000000000273
print(timeit.timeit('calc_range_loop(125)', number=100, globals=globals()))  # N = 125 t = 0.004292299999999971
print(timeit.timeit('calc_range_loop(625)', number=100, globals=globals()))  # N = 625 t = 0.025890899999999994
print(timeit.timeit('calc_range_loop(3125)', number=100, globals=globals()))  # N = 3125 t = 0.11894529999999998


cProfile.run('calc_range_loop(5)')
# 1    0.000    0.000    0.000    0.000 task_1.py:48(calc_range_loop)
cProfile.run('calc_range_loop(25)')
# 1    0.000    0.000    0.000    0.000 task_1.py:48(calc_range_loop)
cProfile.run('calc_range_loop(125)')
# 1    0.000    0.000    0.000    0.000 task_1.py:48(calc_range_loop)
cProfile.run('calc_range_loop(625)')
# 1    0.000    0.000    0.000    0.000 task_1.py:48(calc_range_loop)
cProfile.run('calc_range_loop(3125)')
# 1    0.001    0.001    0.001    0.001 task_1.py:48(calc_range_loop)

# Видим, что самое оптимальное решение - циклом(№3). Нет сильного выигрыша перед рекурсией, 
# так как количество вложенных вызовов линейно увеличивается с ростом N, но видно, что t меньше при больших N 
# в варианте с циклом(в рекурсии происходят затраты на добавление очередных функций в стек). В варианте решение №2 вложен цикл для 
# подсчета очередного члена каждый раз, и время выполнения этого алгоритма возрастает квадратично(наименее эффективное решение)