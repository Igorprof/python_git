str_user = input('Введите строку с пробелами: ')

words = str_user.split(' ')

for i, word in enumerate(words):
    print(f'{i+1}) {word[:10]}')