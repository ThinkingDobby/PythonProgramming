import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input()) - 6
    f = 3 + n // 3
    s = 2 + n // 3
    t = 1 + n // 3
    if n % 3 == 2:
        f += 1
        s += 1
    elif n % 3 == 1:
        f += 1

    print(s, f, t)