import sys

input = sys.stdin.readline

n, x = map(int, input().split())

flag = True
minv, maxv = sorted(map(int, input().split()))
for _ in range(1, n):
    a, b = map(int, input().split())
    minv = max(minv, min(a, b))
    maxv = min(maxv, max(a, b))
    if minv > maxv:
        flag = False

if flag:
    if x in range(minv, maxv + 1):
        print(0)
    else:
        print(min(abs(minv - x), abs(maxv - x)))
else:
    print(-1)
