import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(input().rstrip()) for _ in range(n)]

cnt = 0
for i in range(n - 1):
    for j in range(m - 1):
        if {data[i][j], data[i + 1][j], data[i][j + 1], data[i + 1][j + 1]} == {'f', 'a', 'c', 'e'}:
            cnt += 1

print(cnt)