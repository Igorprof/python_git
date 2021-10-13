print('Введите три стороны треугольника: ')

print('Сторона a: ')
a = int(input())
print('Сторона b: ')
b = int(input())
print('Сторона c: ')
c = int(input())

if (a + b > c) and (a + c > b) and (b + c > a):
    print('Треульник существует!')
    if (a == b == c):
        print('Равносторонний')
    elif (a == b) or (a == c) or (b == c):
        print('Ранобедренный')
    else:
        print('Разносторонний')
else:
    print('Треугольника не существует')