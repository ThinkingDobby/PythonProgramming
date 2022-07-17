import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
memo = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(0, 2 * m, 2):
        memo[i][j // 2] = data[i][j] or data[i][j + 1]

cnt = 0
for i in range(n):
    cnt += memo[i].count(True)

print(cnt)