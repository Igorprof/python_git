from sys import argv

script_name, hours, money_per_hour, prize = argv

salary = int(hours) * int(money_per_hour) + int(prize)

print(f'{script_name}: Зарплата сотрудника составляет {salary} руб.')