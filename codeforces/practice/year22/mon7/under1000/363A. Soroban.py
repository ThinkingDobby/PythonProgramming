import sys

input = sys.stdin.readline

n = input().rstrip()

for i in range(len(n)):
    tmp = int(n[-(i + 1)])
    if tmp >= 5:
        tmp -= 5
        print('-O|', end='')
    else:
        print('O-|', end='')

    for _ in range(tmp):
        print('O', end='')
    print('-', end='')
    for _ in range(5 - tmp - 1):
        print('O', end='')

    print()

