import sys

input = sys.stdin.readline

for _ in range(int(input())):
    w, d, h = map(int, input().split())
    a, b, f, g = map(int, input().split())

    ans = min(a + f + abs(b - g), w - a + w - f + abs(b - g), b + g + abs(a - f), d - b + d - g + abs(a - f)) + h
    print(ans)