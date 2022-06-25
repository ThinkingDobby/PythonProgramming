import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())

    if a > b:
        while a or b:
            if a:
                print("0", end='')
                a -= 1
            if b:
                print("1", end='')
                b -= 1
    else:
        while a or b:
            if b:
                print("1", end='')
                b -= 1
            if a:
                print("0", end='')
                a -= 1

    print()