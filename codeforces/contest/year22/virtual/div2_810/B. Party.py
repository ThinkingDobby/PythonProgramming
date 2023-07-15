import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    cnts = [0 for _ in range(n)]
    qs = []
    for _ in range(m):
        x, y = map(lambda x: int(x) - 1, input().split())
        cnts[x] += 1
        cnts[y] += 1
        qs.append([x, y])

    if m % 2 == 0:
        print(0)
    else:
        odds = []
        for i in range(n):
            if cnts[i] % 2 == 1:
                odds.append([i, a[i]])

        tmp = math.inf
        if odds:
            tmp = sorted(odds, key=lambda x: x[1])[0][1]

        for x, y in qs:
            if cnts[x] % 2 == 0 and cnts[y] % 2 == 0:
                tmp = min(tmp, a[x] + a[y])

        print(tmp)
