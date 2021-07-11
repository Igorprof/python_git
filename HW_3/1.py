def divide(x, y):
    result = x/y
    return result

try:
    a = float(input('Введите делимое: '))
    b = float(input('Введите делитель: '))
except ValueError:
    print('Вводимые значения должны быть числами!')
else:
    try:
        res = divide(a, b)
        print(f'Результат: {res}')
    except ZeroDivisionError:
        print('Деление на ноль невозможно!')

