import collections
import heapq
import math
import sys

input = sys.stdin.readline


def dijkstra(graph, start):
    dists = [math.inf] * (len(graph))
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if dists[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if dists[i[0]] > cost:
                dists[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    memo = []

    for i in dists:
        if i != math.inf:
            memo.append(i)

    return len(memo), max(memo)


n, m, c = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n + 1)]

for i in data:
    graph[i[0]].append([i[1], i[2]])

print(*dijkstra(graph, c))