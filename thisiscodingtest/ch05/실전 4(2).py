import collections

n, m = map(int, input().split())
data = [list(map(int, input())) for i in range(n)]

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(x, y):
    q = collections.deque()
    q.append((x, y))

    while q:
        now = q.popleft()
        for i, j in move:
            a = now[0] + i
            b = now[1] + j
            if 0 <= a < n and 0 <= b < m:
                if data[a][b] == 1:
                    data[a][b] += data[now[0]][now[1]]
                    q.append((a, b))


bfs(0, 0)
print(data[n - 1][m - 1])