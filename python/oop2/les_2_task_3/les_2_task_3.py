# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

n = str(input())
res = ''
for i in n:
    res = f'{i}{res}'

print(f'res - {res}')