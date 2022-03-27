import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, b, x, y = map(int, input().split())

    now = 0
    s = 0
    for i in range(1, n + 1):
        if now + x <= b:
            now += x
        else:
            now -= y
        s += now

    print(s)