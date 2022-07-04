import sys

input = sys.stdin.readline

n, c = map(int, input().split())
data = list(map(int, input().split()))

cnt = 1
for i in range(1, n):
    if data[i] - data[i - 1] <= c:
        cnt += 1
    else:
        cnt = 1

print(cnt)