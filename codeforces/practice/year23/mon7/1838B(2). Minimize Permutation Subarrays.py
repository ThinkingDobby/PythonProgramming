import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    oi = data.index(1)
    ti = data.index(2)

    f = min(oi, ti) + 1
    s = max(oi, ti) + 1
    mi = data.index(n) + 1

    if mi > s:
        print(s, mi)
    elif mi < f:
        print(mi, f)
    else:
        print(1, 1)
