numbers = [5, 4, 3, 2, 6, 3, 5, 7, 2, 4, 5, 9, 0, 1]

res_numbers = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i-1]]

print('Элементы, большие своих левых соседей: ')
for num in res_numbers:
    print(num, end=' ')