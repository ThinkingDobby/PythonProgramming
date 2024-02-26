import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())

    if k >= 4 * n - 4:
        print(k - 2 * n + 2)
    else:
        print((k + 1) // 2)
