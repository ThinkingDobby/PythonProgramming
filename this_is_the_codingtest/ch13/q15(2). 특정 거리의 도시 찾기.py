import collections
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

routes = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    routes[a].append(b)

visited = [False] * (n + 1)
dist = [0] * (n + 1)

dq = collections.deque()
dq.append([x, 0])
visited[x] = True

while dq:
    tmp, cnt = dq.popleft()
    for i in routes[tmp]:
        if not visited[i]:
            dq.append([i, cnt + 1])
            visited[i] = True
            dist[i] = cnt + 1

tmp = [print(i) for i in range(1, n + 1) if dist[i] == k]
if len(tmp) == 0:
    print(-1)