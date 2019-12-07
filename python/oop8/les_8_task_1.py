# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

# graph = [
#     [0, 1, 1],
#     [1, 0, 1],
#     [1, 1, 0]
# ]

import operator
from functools import reduce


graph = []

n = int(input('Введите кол-во человек'))
for i in range(n):
    graph.append([])
    for j in range(n):
        current_value = 1 if i != j else 0
        graph[i].append(current_value)

print(graph)
flat_graph = reduce(operator.concat, graph)
qty = int(sum(flat_graph)/2)
print(qty)
