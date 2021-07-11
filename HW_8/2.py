class ZeroDiv(Exception):
    def __init__(self, text):
        self.txt = text

try:
    m = float(input('Введите делимое: '))
    n = float(input('Введите делитель: '))
    if n == 0:
        raise ZeroDiv('Деление на 0 запрещено!')
    res = m/n 
    print(res)
except ValueError:
    print('Введённые значения должны быть числами!')
except ZeroDiv as ZD:
    print(ZD)