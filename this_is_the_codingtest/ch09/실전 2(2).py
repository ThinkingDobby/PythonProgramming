import collections
import sys

input = sys.stdin.readline


def bfs(graph, start, target):
    q = collections.deque()
    visited = [False] * len(graph)

    q.append([start, 0])
    visited[start] = True

    dist = -1
    while q:
        now, lev = q.pop()

        for i in graph[now]:
            if not visited[i]:
                q.append([i, lev + 1])
                visited[i] = True
                if i == target:
                    dist = lev + 1
                    break

    return dist


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    f, t = map(int, input().split())
    graph[f].append(t)
    graph[t].append(f)
x, k = map(int, input().split())

first = bfs(graph, 1, k)
second = bfs(graph, k, x)
print(-1 if first == -1 or second == -1 else first + second)

