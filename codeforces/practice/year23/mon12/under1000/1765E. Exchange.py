import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b = map(int, input().split())

    if a > b:
        print(1)
    else:
        print((n + a - 1) // a)