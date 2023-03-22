import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())

    if b > d or c + b - a > d:
        print(-1)
    else:
        print((d - b) * 2 + a - c)