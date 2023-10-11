import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
degrees = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]

for f, c in edges:
    degrees[c] += 1
    graph[f].append(c)

dq = collections.deque()
dq.append(degrees[1:].index(0) + 1)

while dq:
    now = dq.popleft()
    print(now)

    for i in graph[now]:
        degrees[i] -= 1

        if degrees[i] <= 0:
            dq.append(i)

"""
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""