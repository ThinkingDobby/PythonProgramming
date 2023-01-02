import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().rstrip()))

    now = data[0]
    for i in range(1, n):
        if data[i] == 1:
            if now > 0:
                print('-', end='')
                now -= 1
            else:
                print('+', end='')
                now += 1
        else:
            print('+', end='')

    print()