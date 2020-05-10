class NotANumber(Exception):
    def __init__(self, text):
        self.txt = text

my_list = []

print('Введите элементы списка(/ для завершения)')

while (True):
    el = input()
    if el == '/':
        break
    my_list.append(el)

try:
    for el in my_list:
        print(el, end = ' ')
        if el.startswith('-'):
            el = el[1:]
        if not el.isdigit():
            raise NotANumber('В списке дожны быть только числа!')
except NotANumber as NaN:
    print(NaN)

