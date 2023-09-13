import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x1, y1, x2, y2 = map(int, input().split())

    ans = abs(min([x1, y1, n - x1 + 1, n - y1 + 1]) - min([x2, y2, n - x2 + 1, n - y2 + 1]))
    print(ans)