import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

f = data.count(1)
s = n - f

tmp = max(0, s - k)

ans = max(0, f + tmp - m)

print(ans)