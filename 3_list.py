﻿n = int(input('Введите номер месяца от 1 до 12: '))

while (n < 1) or (n > 12):
    n = int(input('Повторите ввод: '))

seasons = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']

season = seasons[n-1]

print(f'Время года: {season}')