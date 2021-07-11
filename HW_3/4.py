def my_func(x, y):
    return x**y

def my_func2(x, y):
    res = 1
    for _ in range(abs(y)):
        res *= x

    res = 1/res
    return res

res_1 = round(my_func(2, -1), 4)
res_2 = round(my_func(2, -4), 4)
res_3 = round(my_func2(3, -1), 4)
res_4 = round(my_func2(5, -2), 4)

print(res_1)
print(res_2)
print(res_3)
print(res_4)