numbers_dict = {'one':'один', 'two':'два', 'three':'три', 'four':'четыре'}

with open('4.txt', 'r', encoding='utf-8') as f:
    with open('4_res.txt', 'w', encoding='utf-8') as f_res:
        for line in f.readlines():
            number_str, _, number = line.split()
            new_line = f'{numbers_dict[number_str.lower()].capitalize()} {_} {number}'
            f_res.write(new_line + '\n')