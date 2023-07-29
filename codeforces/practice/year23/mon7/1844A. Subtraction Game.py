import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())

    if a == 1:
        print(3 if b == 2 else 2)
    else:
        print(a - 1)
