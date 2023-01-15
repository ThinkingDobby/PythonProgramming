import sys

input = sys.stdin.readline

n, d = map(int, input().split())
data = list(map(int, input().split()))

cnt = 2
for i in range(n - 1):
    if data[i] + d == data[i + 1] - d:
        cnt += 1
    elif data[i] + d < data[i + 1] - d:
        cnt += 2

print(cnt)
