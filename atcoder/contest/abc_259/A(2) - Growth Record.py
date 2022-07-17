import sys

input = sys.stdin.readline

n, m, x, t, d = map(int, input().split())
base = t - x * d
print(min(t, base + m * d))