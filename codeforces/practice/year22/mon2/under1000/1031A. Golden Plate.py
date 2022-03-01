import sys

input = sys.stdin.readline

w, h, k = map(int, input().split())
s = 0
for _ in range(k):
    s += (w + h - 2) * 2
    w -= 4
    h -= 4

    if w <= 1 or h <= 1:
        break

print(s)