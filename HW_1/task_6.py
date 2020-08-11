print('Введите номер буквы в английском алфавите(целое число от 1 до 26)')

n = int(input())

letter = chr(ord('a') + n - 1)

print(f'Это буква {letter}')