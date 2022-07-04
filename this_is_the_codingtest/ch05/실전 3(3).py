# BFS

import collections

n, m = map(int, input().split())

data = [list(map(int, input())) for _ in range(n)]

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

q = collections.deque()

cnt = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            cnt += 1
            data[i][j] = 1
            q.append((i, j))
            while q:
                now = q.popleft()
                for a, b in move:
                    x = a + now[0]
                    y = b + now[1]
                    if 0 <= x < n and 0 <= y < m:
                        if data[x][y] == 0:
                            data[x][y] = 1
                            q.append((x, y))

print(cnt)
