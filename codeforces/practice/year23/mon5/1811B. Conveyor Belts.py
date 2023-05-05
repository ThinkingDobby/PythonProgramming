import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x1, y1, x2, y2 = map(int, input().split())

    tmp = [abs(x1 - x2), abs(n - y1 + 1 - x2), abs(y1 - y2), abs(n - x1 + 1 - y2), abs(n - y2 + 1 - x1), abs(n - x2 + 1 - y1)]
    print(tmp)
    print(min(tmp))