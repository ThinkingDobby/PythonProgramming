import sys

n, t = map(int, input().split())
data = [list(map(int, input().split())) for i in range(n)]

mv = sys.maxsize
idx = -1
for i in range(n):
    s, d = data[i]
    now = max(((t - s + d - 1) // d) * d + s, s) - t
    if now < mv:
        mv = now
        idx = i

print(idx + 1)