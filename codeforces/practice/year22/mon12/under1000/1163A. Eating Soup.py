import sys

input = sys.stdin.readline

n, m = map(int, input().split())

tmp = n // 2
if m <= tmp:
    print(1 if m == 0 else m)
else:
    print(n - m)