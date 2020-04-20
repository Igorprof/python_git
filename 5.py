my_list = [7, 5, 3, 3, 2]

new_score = 0

while (new_score != 1):
    new_score = int(input('Введите элемент рейтинга: '))

    for i, elem in enumerate(my_list):
        if elem < new_score:
            my_list.insert(i, new_score)
            break

    if i == len(my_list) - 1:
        my_list.append(new_score)    
    
    print(f'Результат: {str(my_list)[1:-1]}')