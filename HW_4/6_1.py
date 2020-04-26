from itertools import count

try:
    start = int(input('Введите стартовое число: '))
except ValueError:
    start = 0

for i in count(start):
    print(i)
    
