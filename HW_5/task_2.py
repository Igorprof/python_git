# Написать программу сложения двух шестнадцатеричных чисел. 
# При этом каждое число представляется как коллекция, элементы которой — цифры числа. 

from collections import deque

digits = '0123456789ABCDEF'
nums = [i for i in range(16)]
dig = dict(zip(digits, nums))
dig_16 = dict(zip(nums, digits))

num1 = deque(input('Введите первое число: '))
num2 = deque(input('Введите второе число: '))

num_res = deque()

for _ in range(abs(len(num1) - len(num2))):
    if len(num1) > len(num2):
        num2.appendleft('0')
    else:
        num1.appendleft('0')

c = 0

for i in range(len(num1) - 1, -1, -1):
    digit_10 = dig[num1[i]] + dig[num2[i]] + c
    if digit_10 >= 16:
        digit_10 -= 16
        c = 1
    else:
        c = 0
    num_res.appendleft(dig_16[digit_10])
if c == 1:
    num_res.appendleft('1')

print(f"Сумма равна {''.join(num_res)}")