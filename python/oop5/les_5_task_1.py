# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from random import randint, choice
import string
from collections import deque


def random_string(string_length=100):
    letters = string.ascii_lowercase
    return '' . join(choice(letters) for _ in range(string_length))


factories = {}

num = int(input('Введите кол-во предприятий'))
# num = randint(3, 5)
i = 0
while i < num:
    i += 1
    name = input('Введите название предприятия')
    # name = random_string(10)
    factories[name] = deque()
    j = 0
    while j < 4:
        j += 1
        income = input(f'Введите прибыль за квартал {j+1}')
        # income = randint(500, 1500)
        factories[name].append(income)

print(factories)

factories_annual_income = {}
total_income = 0
for name in factories:
    income = sum(factories[name])
    factories_annual_income[name] = income
    total_income += income
average_income = total_income / num

print(factories_annual_income)
print(average_income)

more_then_average = deque()
less_then_average = deque()

for name in factories_annual_income:
    if factories_annual_income[name] > average_income:
        more_then_average.append(name)
    else:
        less_then_average.append(name)

print(f'more then average factories {more_then_average}')
print(f'less then average factories {less_then_average}')