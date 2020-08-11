print('Введите первую букву')
a = input()
print('Введите вторую букву')
b = input()

if a > b:
    a, b = b, a

start = ord(a) - ord('a') + 1
end = ord(b) - ord('a') + 1

diff = end - start - 1

print(f'Буква {a} находится на позиции {start}, буква {b} на позиции {end}. Количество букв между ними: {diff}')