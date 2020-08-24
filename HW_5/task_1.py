# Пользователь вводит данные о количестве предприятий, 
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия. 
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, 
# чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

n = int(input('Введите количество предприятий '))
companies = defaultdict(int)

for i in range(1, n + 1):
    name = input(f'Наименование предприятия #{i} ')
    ben_1 = int(input('Прибыль за первый квартал: '))
    ben_2 = int(input('Прибыль за второй квартал: '))
    ben_3 = int(input('Прибыль за третий квартал: '))
    ben_4 = int(input('Прибыль за четвертый квартал: '))
    companies[name] += sum([ben_1, ben_2, ben_3, ben_4])

sred = sum(companies.values()) / len(companies)

companies_good = [name for name in companies if companies[name] > sred]
companies_bad = [name for name in companies if companies[name] < sred]

print(f'Средняя прибыль: {sred}')
print(f'Предприятия, чья прибыль выше средней: {str(companies_good)[1:-1]}')
print(f'Предприятия, чья прибыль ниже средней: {str(companies_bad)[1:-1]}')