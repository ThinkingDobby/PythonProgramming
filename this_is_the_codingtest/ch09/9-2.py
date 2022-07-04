import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])


def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0

    for i in range(n):
        now = heapq.heappop(q)
        while visited[now[1]] and q:
            now = heapq.heappop(q)

        visited[now[1]] = True
        for j in graph[now[1]]:
            if now[0] + j[1] < distance[j[0]]:
                distance[j[0]] = now[0] + j[1]
                heapq.heappush(q, [now[0] + j[1], j[0]])


dijkstra(1)
print(*distance[1:])