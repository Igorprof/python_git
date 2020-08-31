# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. 

import random
# используем "сортировку кучей"
def heapify(nums, heap_size, root_index):  
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)


def heap_sort(nums):  
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)
 
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


array = [random.randint(0, 20) for _ in range(2*random.randint(1, 9) + 1)]

print(array)

heap_sort(array)

median = array[len(array) // 2]

print(f'Медиана равна {median}')