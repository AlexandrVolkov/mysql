# 4. Определить, какое число в массиве встречается чаще всего.

import random


def func(array):
    i = 0
    temp = {}
    while i < len(array):
        if temp.get(array[i]):
            temp[array[i]] += 1
        else:
            temp[array[i]] = 1
        i += 1
    max_number = 0
    max_coincidence = 0
    for i in temp:
        if temp[i] > max_coincidence:
            max_coincidence = temp[i]
            max_number = i
    return max_number


a = [random.randint(0, 5) for _ in range(20)]

print(a)
print(func(a))
