# TLE (BFS)

import collections
import sys

input = sys.stdin.readline

dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

for _ in range(int(input())):
    n, m, sx, sy, d = map(int, input().split())
    sx -= 1
    sy -= 1

    dq = collections.deque()
    dist = [[-1] * m for _ in range(n)]

    dq.append((0, 0))
    dist[0][0] = 0

    while dq:
        x, y = dq.popleft()

        for i, j in dirs:
            nx = x + i
            ny = y + j

            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
                if abs(sx - nx) + abs(sy - ny) > d:
                    dist[nx][ny] = dist[x][y] + 1
                    dq.append((nx, ny))

    print(dist[n - 1][m - 1])
