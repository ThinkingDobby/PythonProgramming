def dfs(now, graph, visited):
    visited[now] = True
    print(now)

    for i in graph[now]:
        if not visited[i]:
            dfs(i, graph, visited)


data = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
dfs(1, data, visited)