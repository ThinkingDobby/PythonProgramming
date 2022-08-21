import collections
import sys

input = sys.stdin.readline


def dfs():
    moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    dq = collections.deque(base)

    while dq:
        now = dq.popleft()
        if now[3] == s:
            break
        for x, y in moves:
            if 0 <= now[0] + x < n and 0 <= now[1] + y < n and data[now[0] + x][now[1] + y] == 0:
                data[now[0] + x][now[1] + y] = now[2]
                dq.append([now[0] + x, now[1] + y, now[2], now[3] + 1])


n, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
s, a, b = map(int, input().split())

base = []
for i in range(n):
    for j in range(n):
        if data[i][j] != 0:
            base.append([i, j, data[i][j], 0])
base.sort(key=lambda x: x[2])

dfs()
print(0 if data[a - 1][b - 1] == 0 else data[a - 1][b - 1])