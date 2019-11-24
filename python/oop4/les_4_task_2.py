# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
# >>> sieve(2)
# 3
# >>> prime(4)
# 7
# >>> sieve(5)
# 11
# >>> prime(1)
# 2

def sieve(n):
    count = 0
    x = 2
    while count < n:
        sieve_list = list(range(n*x + 1))
        sieve_list[1] = 0
        for i in sieve_list:
            if i > 1:
                for j in range(i + i, len(sieve_list), i):
                    sieve_list[j] = 0
        result = list(filter(lambda y: y != 0, sieve_list))
        count = len(result)
        x += 1

    return result[n-1]

# python.exe -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.sieve(10)"
# 100 loops, best of 5: 15.3 usec per loop
#
# python.exe -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.sieve(50)"
# 100 loops, best of 5: 166 usec per loop
#
# python.exe -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.sieve(100)"
# 100 loops, best of 5: 488 usec per loop
#
# python.exe -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.sieve(200)"
# 100 loops, best of 5: 1.37 msec per loop
#
# python.exe -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.sieve(400)"
# 100 loops, best of 5: 2.75 msec per loop

# python.exe -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.sieve(800)"
# 100 loops, best of 5: 7.29 msec per loop

# python.exe -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.sieve(1600)"
# 100 loops, best of 5: 18.4 msec per loop


# сложность O(n)


def prime(n):
    result = [2]
    current = 3
    while len(result) < n:
        if all(current % i != 0 for i in result):
            result.append(current)
        current += 2
    return result[-1]


# python.exe -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.prime(10)"
# 100 loops, best of 5: 10.4 usec per loop

# python.exe -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.prime(50)"
# 100 loops, best of 5: 155 usec per loop

# python.exe -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.prime(100)"
# 100 loops, best of 5: 518 usec per loop

# python.exe -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.prime(200)"
# 100 loops, best of 5: 1.87 msec per loop

# python.exe -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.prime(400)"
# 100 loops, best of 5: 7.22 msec per loop

# python.exe -m timeit -n 100 -s "import les_4_task_2" "les_4_task_2.prime(800)"
# 100 loops, best of 5: 28 msec per loop

# сложность O(n)