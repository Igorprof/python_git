numbers = [5, 4, 10, 3, 5, 6, 2, 6, 3, 5, 2, 7, 2, 4, 5, 9, 0, 1]

res_numbers = [numbers[i] for i in range(len(numbers)) if numbers[i] not in (numbers[:i] + numbers[i+1:])]

print('Элементы, не имеющие повторений: ')
for num in res_numbers:
    print(num, end=' ')


