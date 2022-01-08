# DFS - Stack

n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)]

move = [(0, 1), (0, -1), (-1, 0), (1, 0)]

stack = []
cnt = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            cnt += 1
            data[i][j] = 1
            stack.append((i, j))
            while stack:
                (x, y) = stack[-1]
                flag = True
                for a, b in move:
                    if 0 <= x + a < n and 0 <= y + b < m:
                        if data[x + a][y + b] == 0:
                            data[x + a][y + b] = 1
                            stack.append((x + a, y + b))
                            flag = False
                            break
                if flag:
                    stack.pop()

print(cnt)