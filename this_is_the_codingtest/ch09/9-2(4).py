import heapq
import math
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())
data = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n + 1)]

for f, t, c in data:
    graph[f].append([t, c])

visited = [False] * (n + 1)
dist = [math.inf] * (n + 1)

heap = []
for i in graph[start]:
    dist[i[0]] = i[1]
    heapq.heappush(heap, [i[1], i[0]])

visited[start] = True
dist[start] = 0

while heap:
    c, new = heapq.heappop(heap)
    if not visited[new]:
        visited[new] = True
        for i in graph[new]:
            if dist[i[0]] > dist[new] + i[1]:
                dist[i[0]] = dist[new] + i[1]
                heapq.heappush(heap, [dist[i[0]], i[0]])
        now = new

print(dist[1:])

