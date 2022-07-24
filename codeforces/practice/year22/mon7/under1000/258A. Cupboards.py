import sys

input = sys.stdin.readline

f = 0
s = 0

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    f += a
    s += b

print(min(f, n - f) + min(s, n - s))