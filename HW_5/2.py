with open('2.txt', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines()):
        print(f'Строка#{i+1}. Количество слов: {len(line.split(" "))}')
        
print(f'Всего строк: {i+1}')