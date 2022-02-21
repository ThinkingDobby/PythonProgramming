import sys

input = sys.stdin.readline

x, y, z = map(int, input().split())

if abs(x - y) > z or z == 0:
    if x < y:
        print('-')
    elif x > y:
        print('+')
    else:
        print(0)
else:
    print('?')