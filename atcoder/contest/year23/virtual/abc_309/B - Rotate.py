# unsolved

import sys

input = sys.stdin.readline

n = int(input())
data = [list(input().rstrip()) for _ in range(n)]

tmp = data[0] + [data[i][n - 1] for i in range(1, n - 1)] + data[n - 1][::-1] + [data[i][0] for i in range(n - 2, 0, -1)]
print(tmp)

now = -1
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n - 1 or j == n - 1:
            print(tmp[now], end='')
            now += 1
        else:
            print(data[i][j], end='')
    print()
