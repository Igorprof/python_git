print('Введите несколько строк. Для оканчания введите пустую строку: ')

with open('user_text.txt', 'w', encoding='utf-8') as f:
    while (True):   
        s = input('')
        if s == '':
            break
        f.write(s + '\n')
