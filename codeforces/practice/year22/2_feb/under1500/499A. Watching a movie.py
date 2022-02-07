n, x = map(int, input().split())
data = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]

s = 0
for i in range(1, n + 1):
    tmp = data[i][0] - (data[i - 1][1] + 1)
    s += tmp % x + data[i][1] - data[i][0] + 1

print(s)