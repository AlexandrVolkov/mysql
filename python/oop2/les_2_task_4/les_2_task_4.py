# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

n = int(input())
res = 0
num = 1
for i in range(n):
    if i % 2 == 0:
        res += num
    else:
        res -= num
    num /= 2

print(f'res = {res}')

