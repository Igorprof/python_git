import timeit
import cProfile

def sieve(n):
    total = 2500

    sieve = [i for i in range(total)]  
    sieve[1] = 0

    for i in range(2, total):
        if sieve[i] != 0:
            j = i + i
            while j < total:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    return res[n - 1]


def prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num//2 + 1):
            if num % i == 0:
                return False
        return True

    i = 0
    num = 0
    while (i < n):
        num += 1
        if is_prime(num):
            i += 1        
    return num


print(timeit.timeit('sieve(5)', number=100, globals=globals()))  # N = 5 t = 0.4701377
print(timeit.timeit('sieve(20)', number=100, globals=globals()))  # N = 20 t = 0.25647300000000006
print(timeit.timeit('sieve(80)', number=100, globals=globals()))  # N = 80 t = 0.19262539999999995
print(timeit.timeit('sieve(320)', number=100, globals=globals()))  # N = 320 t = 0.16917780000000004

cProfile.run('sieve(5)')
# 1    0.000    0.000    0.000    0.000 task_2.py:17(<listcomp>)
# 1    0.002    0.002    0.002    0.002 task_2.py:4(sieve)
# 1    0.000    0.000    0.000    0.000 task_2.py:7(<listcomp>)
cProfile.run('sieve(20)')
# 1    0.000    0.000    0.000    0.000 task_2.py:17(<listcomp>)
# 1    0.001    0.001    0.002    0.002 task_2.py:4(sieve)
# 1    0.000    0.000    0.000    0.000 task_2.py:7(<listcomp>)
cProfile.run('sieve(80)')
# 1    0.000    0.000    0.000    0.000 task_2.py:17(<listcomp>)
# 1    0.001    0.001    0.002    0.002 task_2.py:4(sieve)
# 1    0.000    0.000    0.000    0.000 task_2.py:7(<listcomp>)
cProfile.run('sieve(320)')
# 1    0.000    0.000    0.000    0.000 task_2.py:17(<listcomp>)
# 1    0.001    0.001    0.001    0.001 task_2.py:4(sieve)
# 1    0.000    0.000    0.000    0.000 task_2.py:7(<listcomp>)

print('='*20)

print(timeit.timeit('prime(5)', number=100, globals=globals()))  # N = 5 t = 0.0020102000000000037
print(timeit.timeit('prime(20)', number=100, globals=globals()))  # N = 20 t = 0.014607399999999993
print(timeit.timeit('prime(80)', number=100, globals=globals()))  # N = 80 t = 0.1492116
print(timeit.timeit('prime(320)', number=100, globals=globals()))  # N = 320 t = 2.7828188999999997

cProfile.run('prime(5)')
# 1    0.000    0.000    0.000    0.000 task_2.py:20(prime)
# 11    0.000    0.000    0.000    0.000 task_2.py:21(is_prime)
cProfile.run('prime(20)')
# 1    0.000    0.000    0.000    0.000 task_2.py:20(prime)
# 71    0.000    0.000    0.000    0.000 task_2.py:21(is_prime)
cProfile.run('prime(80)')
# 1    0.001    0.001    0.003    0.003 task_2.py:20(prime)
# 409    0.003    0.000    0.003    0.000 task_2.py:21(is_prime)
cProfile.run('prime(320)')
# 1    0.001    0.001    0.032    0.032 task_2.py:20(prime)
# 2129    0.031    0.000    0.031    0.000 task_2.py:21(is_prime)


# Из анализа скорости и сложности двух алгоритмов видим, что алгоритм «Решето Эратосфена» работает за константное время(но изначальный 
# размер массива определен заранее). Время работа второго алгоритма возрастает с ростом N, как и возрастает количество вызовов
# функции проверки прсотое ли число(is_prime)