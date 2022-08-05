import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, h, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    ndata = list(map(lambda x: x[0] * 60 + x[1], data))

    first = 60 * h + m
    cnt = math.inf
    for i in range(n):
        if ndata[i] >= first:
            cnt = min(ndata[i] - first, cnt)
        else:
            cnt = min(24 * 60 - first + ndata[i], cnt)

    print(cnt // 60, cnt % 60)



