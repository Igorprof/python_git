from functools import reduce

evens = [i for i in range(100, 1001) if i % 2 == 0]

mult_all = reduce(lambda total_mult, item: total_mult*item, evens)

print(mult_all)