import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    if n >= 4 or m >= 4:
        print(1, 1)
    else:
        print((n + 1) // 2, (m + 1) // 2)
