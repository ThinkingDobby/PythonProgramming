import sys

input = sys.stdin.readline

x, y, n = map(int, input().split())
f = n % 3 * x
s = min(x * 3, y) * (n // 3)
print(f + s)