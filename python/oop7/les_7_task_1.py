# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.

import random

array = [i for i in range(-100, 100)]
random.shuffle(array)
print(array)


def bubble_sort(array, with_check=0):
    count = 1
    n = 1
    while n < len(array):
        array_is_sorted = 1
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                array_is_sorted = 0
            count += 1
        n += 1
        if with_check and array_is_sorted:
            break
    print(count)
    return array


print(bubble_sort(array[:]))
print(bubble_sort(array[:], True))


# [-48, 99, 93, 81, 21, -16, 52, 62, -85, 19, -81, 63, -8, 23, 10, -52, 11, -44, -55, 24, -41, 70, -7, 58, -66, 1, -47, 76, -35, -4, -49, -71, -6, 91, 48, 14, 92, 53, -21, 83, -87, -42, -89, -63, -97, -99, 96, -26, 15, 74, -3, 7, 88, 17, -68, -86, -40, -24, -19, -20, 50, -82, 85, 39, 47, 16, -96, -67, -56, -5, -73, 94, -58, 66, -45, -92, -59, -69, 18, 31, -64, -22, 38, 27, -70, -100, 67, 54, 71, -77, 0, -51, -36, -2, 78, 69, 77, 42, -28, 4, -30, -62, -13, 84, 98, 61, 59, 80, 8, 44, -38, -50, -33, 22, -98, 97, -29, -72, -65, -14, 28, 60, -54, 51, 82, -37, -60, -10, -94, -34, 56, -1, -83, -90, 87, 25, -18, 26, -75, 45, 34, 68, 46, 6, 57, -80, 5, 12, 75, -91, 33, 73, -53, 2, 65, -9, -25, 37, -12, -57, -46, -76, -31, -15, 95, 36, -39, -84, 72, 86, -23, -11, 40, 30, -32, 49, 90, -74, 3, -17, 89, 79, 20, 9, 32, -88, 43, 13, -43, -78, -79, -93, -61, 41, -27, -95, 29, 55, 35, 64]
# 19901
# [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31, -32, -33, -34, -35, -36, -37, -38, -39, -40, -41, -42, -43, -44, -45, -46, -47, -48, -49, -50, -51, -52, -53, -54, -55, -56, -57, -58, -59, -60, -61, -62, -63, -64, -65, -66, -67, -68, -69, -70, -71, -72, -73, -74, -75, -76, -77, -78, -79, -80, -81, -82, -83, -84, -85, -86, -87, -88, -89, -90, -91, -92, -93, -94, -95, -96, -97, -98, -99, -100]
# 19495
# [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31, -32, -33, -34, -35, -36, -37, -38, -39, -40, -41, -42, -43, -44, -45, -46, -47, -48, -49, -50, -51, -52, -53, -54, -55, -56, -57, -58, -59, -60, -61, -62, -63, -64, -65, -66, -67, -68, -69, -70, -71, -72, -73, -74, -75, -76, -77, -78, -79, -80, -81, -82, -83, -84, -85, -86, -87, -88, -89, -90, -91, -92, -93, -94, -95, -96, -97, -98, -99, -100]
