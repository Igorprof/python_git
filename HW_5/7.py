import json

firms = {}
av_profit = {}
total = 0
k = 0

with open('7.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        name, _, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        firms[name] = profit
        if profit > 0:
            total += profit
            k += 1

av_profit['average_profit'] = total // k if k != 0 else 0

firms_info = [firms, av_profit]

with open('firms.json', 'w', encoding='utf-8') as f_json:
    json.dump(firms_info, f_json, ensure_ascii=False)