import collections
import math
import sys

input = sys.stdin.readline


def get_next_node(memo, now, visited):
    mv = math.inf
    node = -1
    for i in memo[now]:
        if not visited[i[0]] and i[1] < mv:
            mv = i[1]
            node = i[0]

    return node


n, m = map(int, input().split())
start = int(input()) - 1
data = [list(map(int, input().split())) for _ in range(m)]
memo = collections.defaultdict(list)

visited = [False] * n
dist = [math.inf] * n

for f, t, c in data:
    memo[f - 1].append([t - 1, c])

visited[start] = True
dist[start] = 0
for i in memo[start]:
    dist[i[0]] = i[1]

now = start
while not all(visited):
    new = get_next_node(memo, now, visited)

    for i in memo[new]:
        dist[i[0]] = min(dist[i[0]], dist[new] + i[1])

    now = new
    visited[now] = True

print(dist)


