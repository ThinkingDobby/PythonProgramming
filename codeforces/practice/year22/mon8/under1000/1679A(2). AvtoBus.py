import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    if n % 2 == 1 or n < 4:
        print(-1)
    else:
        l = n // 6 if n % 6 == 0 else n // 6 + 1
        h = n // 4
        print(l, h)