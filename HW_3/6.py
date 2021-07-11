def int_func(word):
    # Без использовании функции capitalize
    letters = list(word)
    letters[0] = letters[0].upper()
    cap_word = ''.join(letters)
    return cap_word

s = input('Введите строку: ')
new_s = ''

for word in s.split():
    new_s += int_func(word) + ' '

print(new_s)