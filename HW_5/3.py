total = 0
sred = 0

with open('3.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    k = len(lines)
    for emp in lines:
        family, salary = emp.split()
        if int(salary) < 20000:
            print(family)
        total += int(salary)
    if k != 0:
        sred = total / k
        print(f'Средний оклад: {sred}')