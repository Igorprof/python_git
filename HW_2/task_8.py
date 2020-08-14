# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. 
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

print('Введите количество чисел и искомую цифру: ')

n = int(input('Количество: '))
c = int(input('Искомая цифра: '))
k = 0

for i in range(n):
    cur = input(f'Число #{i+1}: ')
    for digit in cur:
        if int(digit) == c:
            k += 1

print(f'Цифра {c} встречается {k} раз(а)')
