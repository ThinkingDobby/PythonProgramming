import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c, r = map(int, input().split())

    if c - r > max(a, b) or c + r < min(a, b):
        print(max(a, b) - min(a, b))
    else:
        print(max(a, b) - min(a, b) - (min(c + r, max(a, b)) - max(c - r, min(a, b))))
