import sys

input = sys.stdin.readline

n, d = map(int, input().split())
data = list(map(int, input().split()))

cnt = 0
for i in range(1, n):
    if data[i - 1] >= data[i]:
        tmp = (data[i - 1] - data[i] + d) // d
        cnt += tmp
        data[i] = data[i] + tmp * d

print(cnt)
