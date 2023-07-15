import sys

input = sys.stdin.readline

n, m, x, t, d = map(int, input().split())

if n <= x:
    first = t - n * d
else:
    first = t - x * d

print(min(first + d * x, first + d * m))
