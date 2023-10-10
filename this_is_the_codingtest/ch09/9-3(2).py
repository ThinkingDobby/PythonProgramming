import math
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(m)]

memo = [[math.inf] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    memo[i][i] = 0

for f, t, c in data:
    memo[f][t] = c

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            memo[i][j] = min(memo[i][j], memo[i][k] + memo[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(memo[i][j], end=' ')
    print()