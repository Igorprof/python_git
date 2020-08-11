# https://drive.google.com/file/d/1j7LHRHpuE_4P1xSlZEaCWGySpStBh7fI/view?usp=sharings

print('Введите трехзначное число: ')
number = int(input())

s = 0
pr = 1

o = number % 10
number //= 10

s += o
pr *= o

o = number % 10
number //= 10

s += o
pr *= o

o = number % 10

s += o
pr *= o

print(f'Сумма: {s}\nПроизведение: {pr}')