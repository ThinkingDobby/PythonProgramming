import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = sorted(map(lambda x: ord(x) - 96, input().rstrip()))

cnt = 1
tot = data[0]
prev = data[0]
for i in range(1, n):
    if cnt == k:
        break
    if data[i] - prev > 1:
        cnt += 1
        tot += data[i]
        prev = data[i]

print(-1 if cnt != k else tot)
