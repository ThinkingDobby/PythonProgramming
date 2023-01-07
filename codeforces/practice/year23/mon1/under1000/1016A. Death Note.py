import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

tot = 0
ans = []
for i in range(n):
    tot += data[i]
    now = tot // m
    tot = tot % m
    ans.append(now)

print(*ans)