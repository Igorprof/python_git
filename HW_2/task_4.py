# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… 
# Количество элементов (n) вводится с клавиатуры.

def calc_range(cur, n):
    if (n == 1):
        return cur
    return cur + calc_range(cur * (-0.5), n - 1)

print('Введите n')

n = int(input())

s = calc_range(1, n)

print(f'Сумма {n} слагаемых ряда равна {s}')