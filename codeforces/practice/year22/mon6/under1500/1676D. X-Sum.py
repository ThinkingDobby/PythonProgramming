# runtime error

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    memo = [[0] * m for _ in range(n)]

    for i in range(n):
        s = 0
        t1 = i
        t2 = 0
        for _ in range(max(n, m)):
            s += data[t1][t2]
            t1 += 1
            t2 += 1
            if t1 >= n or t2 >= m:
                break
        t1 = i
        t2 = 0
        for _ in range(max(n, m)):
            memo[t1][t2] = s
            t1 += 1
            t2 += 1
            if t1 >= n or t2 >= m:
                break

    for i in range(1, m):
        s = 0
        t1 = 0
        t2 = i
        for _ in range(max(n, m)):
            s += data[t1][t2]
            t1 += 1
            t2 += 1
            if t1 >= n or t2 >= m:
                break
        t1 = 0
        t2 = i
        for _ in range(max(n, m)):
            memo[t1][t2] = s
            t1 += 1
            t2 += 1
            if t1 >= n or t2 >= m:
                break

    for i in range(n):
        data[i] = data[i][::-1]
    for i in range(n):
        memo[i] = memo[i][::-1]

    for i in range(n):
        s = 0
        t1 = i
        t2 = 0
        for _ in range(max(n, m)):
            s += data[t1][t2]
            t1 += 1
            t2 += 1
            if t1 >= n or t2 >= m:
                break
        t1 = i
        t2 = 0
        for _ in range(max(n, m)):
            memo[t1][t2] += (s - data[t1][t2])
            t1 += 1
            t2 += 1
            if t1 >= n or t2 >= m:
                break

    for i in range(1, m):
        s = 0
        t1 = 0
        t2 = i
        for _ in range(max(n, m)):
            s += data[t1][t2]
            t1 += 1
            t2 += 1
            if t1 >= n or t2 >= m:
                break
        t1 = 0
        t2 = i
        for _ in range(max(n, m)):
            memo[t1][t2] += (s - data[t1][t2])
            t1 += 1
            t2 += 1
            if t1 >= n or t2 >= m:
                break

    mv = -1
    for i in range(n):
        mv = max(max(memo[i]), mv)
    print(mv)