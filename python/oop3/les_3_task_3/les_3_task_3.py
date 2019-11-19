# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random


def func(array):
    i = 0
    i_max = 0
    i_min = 0
    while i < len(array):
        if array[i] > array[i_max]:
            i_max = i
        if array[i] < array[i_min]:
            i_min = i
        i += 1
    spam = array[i_min]
    array[i_min] = array[i_max]
    array[i_max] = spam
    return array


a = [random.randint(0, 100) for _ in range(10)]
print(a)
print(func(a))
