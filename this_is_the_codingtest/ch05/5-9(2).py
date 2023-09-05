import collections


def bfs(graph, start, visited):
    dq = collections.deque()
    dq.append(start)
    visited[start] = True

    while dq:
        now = dq.popleft()
        print(now)

        for i in graph[now]:
            if not visited[i]:
                dq.append(i)
                visited[i] = True


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