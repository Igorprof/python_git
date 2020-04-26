def fibo_gen():
    number = 1
    N = 15
    for k in range(1, N+1):
        number *= k
        yield number

for el in fibo_gen():
    print(el, end=' ')
