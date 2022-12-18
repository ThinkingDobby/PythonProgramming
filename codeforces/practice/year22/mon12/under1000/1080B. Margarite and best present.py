import sys

input = sys.stdin.readline

for _ in range(int(input())):
    l, r = map(int, input().split())

    if r == l:
        print(r * (1 if r % 2 == 0 else -1))
    else:
        n = r - l + 1
        s = 0
        if l % 2 == 0:
            s += -(n // 2)
        else:
            s += (n // 2)

        if n % 2 == 1:
            s += r * (1 if r % 2 == 0 else -1)

        print(s)
