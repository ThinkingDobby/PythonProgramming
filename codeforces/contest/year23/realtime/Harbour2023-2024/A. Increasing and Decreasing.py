import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x, y, n = map(int, input().split())

    if y - x >= n * (n - 1) // 2:
        print(x, end=' ')
        now = y - (n - 1) * (n - 2) // 2
        for i in range(n - 2, -1, -1):
            print(now, end=' ')
            now += i
        print()
    else:
        print(-1)