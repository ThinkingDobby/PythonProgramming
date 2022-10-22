import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, x, y = map(int, input().split())

    a, b = sorted([x, y])
    if a != 0:
        print(-1)
    else:
        if b != 0 and (n - 1) % b == 0:
            for i in range(2, n + 1, b):
                for _ in range(b):
                    print(i, end=' ')
            print()
        else:
            print(-1)
