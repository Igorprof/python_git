n = int(input('Число элементов списка: '))

my_list = []
print('Введите список: ')
for i in range(n):
    el = input(f'Элемент {i+1}: ')
    my_list.append(el)

for i in range(1, n, 2):
    t = my_list[i]
    my_list[i] = my_list[i-1]
    my_list[i-1] = t

print(my_list)