# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые необходимо обойти.

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    path = {}
    cost[start] = 0

    min_cost = 0
    s = start

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    for i in range(length):
        if cost[i] != float('inf'):
            path[i] = []
        else:
            path[i] = ['Нет маршрута']

    for i in range(length):
        if cost[i] != float('inf'):
            k = i
            # path[i].append(s)
            path[i].append(k)
            while k > 0 and parent[k] != s:
                if i != s:
                    path[i].append(parent[k])
                k = parent[k]
            if parent[k] == s:
                path[i].append(parent[k])

    for i in range(length):
        path[i] = path[i][::-1]

    result = {}

    for i in range(length):
        result[i] = {}
        result[i]['cost'] = cost[i]
        result[i]['path'] = path[i]

    return result


s = int(input('От какой вершины идти: '))
print(dijkstra(g, s))