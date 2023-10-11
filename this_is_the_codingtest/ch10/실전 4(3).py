import collections
import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
time = [0] * (n + 1)
result = [0] * (n + 1)
degrees = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))[:-1]
    time[i] = data[0]
    result[i] = data[0]

    for j in data[1:]:
        graph[j].append(i)
    degrees[i] = len(data[1:])

dq = collections.deque()
dq.append(degrees[1:].index(0) + 1)

while dq:
    now = dq.pop()

    for i in graph[now]:
        degrees[i] -= 1
        if degrees[i] <= 0:
            dq.append(i)

        result[i] = max(time[i] + result[now], result[i])

print(*result[1:])

"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""

