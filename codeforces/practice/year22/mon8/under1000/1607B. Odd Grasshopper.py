import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x, n = map(int, input().split())

    if x % 2 == 0:
        if n % 4 == 0:
            tmp = 0
        elif n % 4 == 1:
            tmp = -(1 + n // 4 * 4)
        elif n % 4 == 2:
            tmp = 1
        else:
            tmp = 4 + n // 4 * 4
        print(x + tmp)
    else:
        if n % 4 == 0:
            tmp = 0
        elif n % 4 == 1:
            tmp = 1 + n // 4 * 4
        elif n % 4 == 2:
            tmp = -1
        else:
            tmp = -(4 + n // 4 * 4)
        print(x + tmp)

