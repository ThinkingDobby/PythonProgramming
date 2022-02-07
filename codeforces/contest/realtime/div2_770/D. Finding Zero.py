# WA
# 쿼리 최소화가 관건

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    memo = {}
    midx = [-1, -1, -1]
    mv = -1
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                print('?', i, j, k)
                sys.stdout.flush()
                data = int(input())
                memo[(i, j, k)] = data
                if data > mv:
                    mv = data
                    midx = (i, j, k)

    tmp = -1
    for i in range(1, n + 1):
        if i not in midx:
            tmp = i
            break

    if memo[tuple(sorted([midx[0], midx[1], tmp]))] == mv:
        print('!', midx[0], midx[1])
    elif memo[tuple(sorted([midx[0], midx[2], tmp]))] == mv:
        print('!', midx[0], midx[2])
    else:
        print('!', midx[1], midx[2])
    sys.stdout.flush()