# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
import random


def generate_graph(n):
    graph = []
    for i in range(n):
        graph.append([])
        for j in range(random.randint(1, n // 2)):
            while True:
                x = random.randint(0, n - 1)
                if x != i and x not in graph[i]:
                    break
            graph[i].append(x)
    return graph


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        for i in graph[vertex]:
            if i not in visited:
                stack.append(i)
        visited.add(vertex)
    return visited


n = int(input('Введите кол-во вершин: '))
graph = generate_graph(n)
print(graph)
# graph = [[4, 1, 2], [0, 3], [3], [0, 2, 4], [3, 0]]

print(dfs(graph, 1))
