import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))

    oi = data.index(1)
    ti = data.index(2)
    mi = data.index(n)

    if oi < ti:
        if oi + 1 == ti:
            if oi < mi:
                print(oi + 2, mi + 1)
            else:
                print(oi + 1, mi + 1)
        else:
            print(oi + 2, mi + 1)
    else:
        if oi - 1 == ti:
            if oi < mi:
                print(oi + 1, mi + 1)
            else:
                print(oi, mi + 1)
        else:
            print(oi, mi + 1)
