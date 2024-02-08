import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m, sx, sy, d = map(int, input().split())

    if sx - d <= 1 and sx + d >= n or sy - d <= 1 and sy + d >= m:
        print(-1)
    else:
        print(n - 1 + m - 1)