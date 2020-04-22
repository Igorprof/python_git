def my_func(x_1, x_2, x_3):
    x = (x_1, x_2, x_3)
    return sum(x) - min(x)

my_sum = my_func(10, 4, 5)

print(my_sum)
