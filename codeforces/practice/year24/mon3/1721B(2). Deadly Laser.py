import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m, sx, sy, d = map(int, input().split())

    if sx - d <= 1 and sx + d >= n or sy + d >= m and sy - d <= 1 or n - sx + m - sy <= d:
        print(-1)
    else:
        print(n + m - 2)