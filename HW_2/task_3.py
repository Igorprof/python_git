# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
# Например, если введено число 3486, надо вывести 6843.

print('Введите целое число: ')

number = int(input())

res_num = 0

while (number > 0):
    res_num = res_num*10 + number % 10
    number //= 10

print(f'Обратное по порядку цифр число равно {res_num}')