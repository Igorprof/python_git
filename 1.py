my_list = [1, 1.5, True, 'hello', [1, 2, 3], ('1', '2', '3'), {'1':1, '2':2}]

for item in my_list:
    print(f'Элемент {item} имеет тип {type(item)}')