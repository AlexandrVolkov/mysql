# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random
num = 10
array = [random.uniform(0, 50) for i in range(num)]
print(array)


def merge(left, right):
    sorted_array = []
    left_index = right_index = 0
    left_length, right_length = len(left), len(right)
    for _ in range(left_length + right_length):
        if left_index < left_length and right_index < right_length:
            if left[left_index] <= right[right_index]:
                sorted_array.append(left[left_index])
                left_index += 1
            else:
                sorted_array.append(right[right_index])
                right_index += 1
        elif left_index == left_length:
            sorted_array.append(right[right_index])
            right_index += 1
        elif right_index == right_length:
            sorted_array.append(left[left_index])
            left_index += 1
    return sorted_array


def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge(left, right)


print(merge_sort(array))