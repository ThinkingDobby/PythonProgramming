import collections


def bfs(graph, v, visited):
    queue = collections.deque()
    visited[v] = True
    print(v)
    queue.append(v)

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                print(i)
                queue.append(i)

g = [
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

v = [False] * 9

bfs(g, 1, v)