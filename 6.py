n = int(input('Введите количество товаров: '))

goods = []

for i in range(n):
    print(f'Товар №{i+1}')
    name = input('Название: ')
    price = int(input('Цена: '))
    number = int(input('Количество: '))
    measure = input('Единица измерения: ')

    goods.append((i+1, {'название': name, 'цена': price, 'количество': number, 'ед': measure}))

goods_stat = {}

names = []
prices = []
numbers = []
for good in goods:
    names.append(good[1]['название'])
    prices.append(good[1]['цена'])
    numbers.append(good[1]['количество'])

goods_stat['название'] = names
goods_stat['цена'] = prices
goods_stat['количество'] = numbers
goods_stat['ед'] = measure

print(goods_stat)