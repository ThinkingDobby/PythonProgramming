import sys

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if i == j or i == n - j - 1 or i == (n - 1) // 2 or j == (n - 1) // 2:
            cnt += data[i][j]

print(cnt)