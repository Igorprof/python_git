# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, 
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random

def bubble_sort(arr):
    n = 1

    while (n < len(arr)):
        for i in range(len(arr) - n):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                
        n += 1


array = [random.randrange(-100, 100) for _ in range(random.randint(5, 15))]

print(array)

bubble_sort(array)

print(array)