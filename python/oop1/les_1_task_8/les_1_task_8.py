# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).


print("Введите три числа:")
a = int(input())
b = int(input())
c = int(input())

if a <= b <= c or c <= b <= a:
    print('Второе число среднее')
elif b <= a <= c or c <= a <= b:
    print('Первое число среднее')
else:
    print('Третье число среднее')