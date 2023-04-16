# WA

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))

    if n == k:
        print(0 if data == sorted(data) else 1)
    else:
        cnt = 0
        tmp = data[n - 1 - k: n]
        if tmp != sorted(tmp):
            cnt += 1
        maxv = max(tmp)
        minv = min(tmp)

        for i in range(n - 1 - k - 1, -1, -1):
            if data[i] > maxv:
                cnt += 1
                maxv = data[i]
            elif data[i] > minv:
                cnt += 1
                minv = data[i]

        print(cnt)