import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())

    if m % 2 == 1:
        m -= 1

    print(n * m // 2)