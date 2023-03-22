import sys

input = sys.stdin.readline

n, k = map(int, input().split())

cnt = k
data = list(map(int, input().split()))
tot = 0

ans = -1
for i in range(n):
    tot += data[i]
    tmp = min(tot, 8)
    cnt -= tmp
    tot -= tmp
    if cnt <= 0:
        ans = i + 1
        break

print(ans)