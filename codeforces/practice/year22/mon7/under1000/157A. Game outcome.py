import sys

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

row_sum = [0 for _ in range(n)]
col_sum = [0 for _ in range(n)]

for i in range(n):
    for j in range(n):
        row_sum[i] += data[i][j]
        col_sum[j] += data[i][j]

cnt = 0
for i in range(n):
    for j in range(n):
        if row_sum[i] < col_sum[j]:
            cnt += 1

print(cnt)