#  Определить, какое число в массиве встречается чаще всего.

import random
import time
import sys
from gc import get_referents


def get_size(obj):
    seen_ids = set()
    size = 0
    objects = [obj]
    while objects:
        need_referents = []
        for obj in objects:
            if id(obj) not in seen_ids:
                seen_ids.add(id(obj))
                size += sys.getsizeof(obj)
                need_referents.append(obj)
        objects = get_referents(*need_referents)
    return size


def get_total_size(*args):
    total_size = 0
    for a in args:
        total_size += get_size(a)
    return total_size


def func_1(array):
    i = 0
    temp1 = {}
    while i < len(array):
        if temp1.get(array[i]):
            temp1[array[i]] += 1
        else:
            temp1[array[i]] = 1
        i += 1
    max_number = 0
    max_coincidence = 0
    for i in temp1:
        if temp1[i] > max_coincidence:
            max_coincidence = temp1[i]
            max_number = i
    print(get_total_size(temp1, max_coincidence, max_number, i))

    return max_number


def func_2(array):
    temp2 = {}
    for i in array:
        if temp2.get(i):
            temp2[i].append(i)
        else:
            temp2[i] = [i]
    max_number = 0
    max_coincidence = 0
    for i in temp2:
        if len(temp2[i]) > max_coincidence:
            max_coincidence = len(temp2[i])
            max_number = i
    print(get_total_size(temp2, max_coincidence, max_number, i))

    return max_number


def func_3(array):
    temp3 = {}
    for i in array:
        if not temp3.get(i):
            temp3[i] = []
        temp3[i].append({f'Found number {i} - time = {time.time()}'})
    max_number = 0
    max_coincidence = 0
    for i in temp3:
        if len(temp3[i]) > max_coincidence:
            max_coincidence = len(temp3[i])
            max_number = i
    print(get_total_size(temp3, max_coincidence, max_number, i))

    return max_number


a = [random.randint(0, 5) for _ in range(20)]
print(sys.version, sys.platform)
print(a)
print(func_1(a))
print(func_2(a))
print(func_3(a))


# [3, 5, 4, 4, 3, 2, 5, 3, 5, 5, 1, 1, 4, 2, 2, 1, 0, 4, 3, 5]
# 612
# 5
# 1204
# 5
# 7500
# 5

# Лучший вариант func_1, т.к. не тратит дополнительную память на хранение лишних чисел