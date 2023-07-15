# TLE

import sys
import bisect

input = sys.stdin.readline

a = []
l = 0

for _ in range(int(input())):
    data = list(map(int, input().split()))
    if data[0] == 1:
        bisect.insort(a, data[1])
        l += 1
    elif data[0] == 2:
        idx = bisect.bisect_right(a, data[1])
        if idx - data[2] > -1:
            print(a[idx - data[2]])
        else:
            print(-1)
    elif data[0] == 3:
        idx = bisect.bisect_left(a, data[1]) - 1
        if idx + data[2] < l:
            print(a[idx + data[2]])
        else:
            print(-1)