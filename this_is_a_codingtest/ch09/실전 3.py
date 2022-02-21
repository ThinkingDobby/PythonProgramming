import math
import sys
import heapq

input = sys.stdin.readline
INF = math.inf

n, m, c = map(int, input().split())
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist < distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)

cnt = 0
mv = -1
for i in distance:
    if i != INF:
        if i != 0:
            cnt += 1
        mv = max(mv, i)

print(cnt, mv)

"""
3 2 1
1 2 4
1 3 2
"""