import sys

input = sys.stdin.readline

n = int(input())
data = [input().rstrip() for _ in range(n)]

cnt = 0
for i in range(n - 2):
    for j in range(n - 2):
        if data[i][j] == 'X' and data[i + 2][j] == 'X' and data[i + 1][j + 1] == 'X'and data[i][j + 2] == 'X' and data[i + 2][j + 2] == 'X':
            cnt += 1

print(cnt)