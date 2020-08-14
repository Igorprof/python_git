# https://drive.google.com/file/d/1OJEnhl0o87bgD6Tr32LJa6yfyfhIMitn/view?usp=sharing

# Посчитать четные и нечетные цифры введенного натурального числа. 
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

print('Введите натуральное число: ')

n = int(input())
k_odd = 0
k_even = 0

while (n > 0):
    cur = n % 10
    if (cur % 2 == 0):
        k_even += 1
    else:
        k_odd += 1
    n //= 10

print(f'Количество четных цифр: {k_even}, нечетных: {k_odd}')
