import sys

input = sys.stdin.readline

for i in range(int(input())):
    a, b, c = map(int, input().split())

    f = a - 1
    if b > c:
        s = b - 1
    else:
        s = c - b + c - 1

    if f == s:
        print(3)
    elif f < s:
        print(1)
    else:
        print(2)