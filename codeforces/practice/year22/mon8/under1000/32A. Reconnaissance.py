import sys

input = sys.stdin.readline

n, d = map(int, input().split())
data = sorted(map(int, input().split()))

cnt = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        if data[j] - data[i] <= d:
            cnt += 1

print(cnt * 2)