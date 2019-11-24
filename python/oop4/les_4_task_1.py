# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

import random
import timeit
import operator


def test_func(num):
    array = [random.randint(0, 100 * num) for _ in range(num)]
    for i in range(100):
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


# python.exe -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.test_func(10)"
# 100 loops, best of 5: 181 usec per loop
#
# python.exe -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.test_func(100)"
# 100 loops, best of 5: 1.63 msec per loop
#
# python.exe -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.test_func(1000)"
# 100 loops, best of 5: 18.8 msec per loop



def test_func2(num):
    array = [random.randint(0, 100 * num) for _ in range(num)]
    for i in range(100):
        sorted_array = array[:]
        sorted_array.sort()
        min = sorted_array[0]
        max = sorted_array[len(sorted_array) - 1]
        result = []
        for i in array:
            if i == min:
                result.append(max)
            elif i == max:
                result.append(min)
            else:
                result.append(i)
    return result

# python.exe -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.test_func2(10)"
# 100 loops, best of 5: 136 usec per loop
#
# python.exe -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.test_func2(100)"
# 100 loops, best of 5: 1.3 msec per loop
#
# python.exe -m timeit -n 100 -s "import les_4_task_1" "les_4_task_1.test_func2(1000)"
# 100 loops, best of 5: 16.5 msec per loop


# третий вариант сложно придумать


# второй вариант вышел быстрее за счёт использования стандартных функций python по работе с массивами