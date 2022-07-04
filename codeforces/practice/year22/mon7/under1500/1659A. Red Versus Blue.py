import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, r, b = map(int, input().split())
    if r >= b:
        tmp = r // (b + 1)
        print('R' * tmp, end='')
        rest = r % (b + 1)
        if rest:
            print('R', end='')
            rest -= 1
        for _ in range(b):
            print('B', end='')
            print('R' * tmp, end='')
            if rest:
                print('R', end='')
                rest -= 1
    else:
        tmp = b // (r + 1)
        print('B' * tmp, end='')
        rest = b % (r + 1)
        if rest:
            print('B', end='')
            rest -= 1
        for _ in range(r):
            print('R', end='')
            print('B' * tmp, end='')
            if rest:
                print('B', end='')
                rest -= 1

    print()