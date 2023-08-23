import sys

input = sys.stdin.readline

for _ in range(int(input())):
    b, c, h = map(int, input().split())

    tmp = min(b - 1, c + h)
    print(tmp * 2 + 1)