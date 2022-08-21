import collections
import math
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

routes = collections.defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    routes[a].append(b)

visited = [False] * (n + 1)
memo = [math.inf] * (n + 1)


def dfs(now, cnt):
    if cnt > k or cnt > memo[now]:
        return
    visited[now] = True
    memo[now] = min(memo[now], cnt)

    for i in routes[now]:
        if not visited[i]:
            dfs(i, cnt + 1)
            visited[i] = False


dfs(x, 0)
temp = [i for i in range(1, n + 1) if memo[i] == k]
if len(temp) == 0:
    print(-1)
else:
    for i in temp:
        print(i)