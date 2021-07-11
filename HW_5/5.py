import random

with open('5.txt', 'w', encoding='utf-8') as f:
    for _ in range(random.randint(6, 11)):
        f.write(f'{random.randint(0, 99)} ')

with open('5.txt', 'r', encoding='utf-8') as f:
    numbers = list(map(int, f.readline().split()))
    print(sum(numbers))