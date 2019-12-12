# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.

import random
m = 5
size = 2 * m + 1
array = [random.randint(0, 100) for i in range(size)]
random.shuffle(array)
print(array)


def get_median(array):
    n = 0
    while n < len(array) - 1:
        bigger = 0
        smaller = 0
        for i in array:
            if array[n] < i:
                bigger += 1
            if array[n] > i:
                smaller += 1
        if smaller == bigger:
            break
        n += 1

    return array[n]


print(get_median(array))
