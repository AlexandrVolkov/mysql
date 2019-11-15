# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

result = {}
for i in range(2, 10):
    result[i] = 0

for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            result[j] = result[j] + 1

for i in result:
    print(f'{i} => {result[i]}')