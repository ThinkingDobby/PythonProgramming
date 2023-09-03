import sys

input = sys.stdin.readline


def dfs(a, b, now, visited):
    visited[a][b] = True

    for _ in range(4):
        now = (now - 1) % 4
        if 0 <= a + dirs[now][0] < n and 0 <= b + dirs[now][1] < m:
            if data[a + dirs[now][0]][b + dirs[now][1]] == 0 and not visited[a + dirs[now][0]][b + dirs[now][1]]:
                dfs(a + dirs[now][0], b + dirs[now][1], now, visited)


dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

n, m = map(int, input().split())
a, b, now = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dfs(a, b, now, visited)

cnt = 0
for i in visited:
    cnt += i.count(True)

print(cnt)

"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""