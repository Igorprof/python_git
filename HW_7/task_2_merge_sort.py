# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

def merge(left, right):
    result = []
    l, r = 0, 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    while l < len(left):
        result.append(left[l])
        l += 1
    while r < len(right):
        result.append(right[r])
        r += 1
    return result

def merge_sort(arr):
    if len(arr) < 2:
        return arr[:]
    
    middle = int(len(arr) / 2)
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)


array = [random.uniform(0, 50) for _ in range(random.randint(5, 15))]

array_sorted = merge_sort(array)

print(array)
print(array_sorted)