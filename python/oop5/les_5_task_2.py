# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque, defaultdict

letters_value = defaultdict(int)
letters_value.update({'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15})
digit_value = defaultdict(str)
digit_value.update({'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'})


def int_to_hex(result_int):
    result_hex = deque()
    while result_int > 0:
        cur = str(result_int)
        if result_int > 15:
            cur = str(result_int % 16)
            result_int = result_int // 16
        else:
            result_int = 0
        if digit_value[cur]:
            cur = digit_value[cur]
        result_hex.appendleft(cur)
    return result_hex


def hex_to_int(result_hex):
    result_int = 0
    i_num = 0
    for i in result_hex:
        if letters_value[i]:
            i = letters_value[i]
        i = int(i)
        result_int += i * (16 ** i_num)
        i_num += 1
    return result_int


num1 = input('Введите первое число')
num2 = input('Введите второе число')
# num1 = 'A2'
# num2 = 'C4F'
num1 = deque(num1)
num2 = deque(num2)
print(num1, num2, sep='\n')
num1.reverse()
num2.reverse()
num1_int = hex_to_int(num1)
num2_int = hex_to_int(num2)
result_sum = num1_int + num2_int
result_sum_hex = int_to_hex(result_sum)
result_multiply = num1_int * num2_int
result_multiply_hex = int_to_hex(result_multiply)


print(result_sum_hex)
print(result_multiply_hex)