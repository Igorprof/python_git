# В диапазоне натуральных чисел от 2 до 99 определить, 
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

array = [n for n in range(2, 100)]
res = [0] * 8

for n in array:
    for i in range(2, 10):
        if n % i == 0:
            res[i-2] += 1

print(*[f'{i} - {res[i-2]}' for i in range(2, 10)], sep = '\n')