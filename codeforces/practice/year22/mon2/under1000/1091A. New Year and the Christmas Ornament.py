import sys

input = sys.stdin.readline

y, b, r = map(int, input().split())
tmp = min(y, b - 1, r - 2)
print(tmp * 3 + 3)