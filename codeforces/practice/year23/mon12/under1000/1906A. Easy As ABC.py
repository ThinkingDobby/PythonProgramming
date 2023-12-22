import sys

input = sys.stdin.readline

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (1, -1), (-1, 1))

ans = "ZZZ"


def dfs(data, i, j, now, visited):
    global ans
    if now > ans:
        return

    if len(now) >= 3:
        ans = now
        return

    visited[i][j] = True

    for r, c in dirs:
        ni = i + r
        nj = j + c
        if 0 <= ni < 3 and 0 <= nj < 3 and not visited[ni][nj]:
            dfs(data, ni, nj, now + data[i][j], visited)

    visited[i][j] = False


data = [list(input().rstrip()) for _ in range(3)]
visited = [[False] * 3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        dfs(data, i, j, "", visited)

print(ans)