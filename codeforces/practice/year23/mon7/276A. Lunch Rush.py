import math
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

mv = -math.inf
for _ in range(n):
    f, t = map(int, input().split())

    if t > k:
        mv = max(mv, f - (t - k))
    else:
        mv = max(mv, f)

print(mv)