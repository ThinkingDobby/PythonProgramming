# DFS - Recursion

n, m = map(int, input().split())

data = [list(map(int, input())) for i in range(n)]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if data[x][y] == 0:
        data[x][y] = 1

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True

    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)