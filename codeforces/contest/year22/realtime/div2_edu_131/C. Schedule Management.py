# R

import sys

input = sys.stdin.readline


def check(now):
    cnt = 0
    for i in range(1, n + 1):
        if memo[i] <= now:
            cnt += (now - memo[i]) // 2
        else:
            cnt -= memo[i] - now
    return cnt >= 0


for _ in range(int(input())):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    memo = [0 for _ in range(n + 1)]
    for i in data:
        memo[i] += 1

    l = 0
    r = m * 2
    while l < r:
        mid = (l + r) // 2
        if check(mid):
            r = mid
        else:
            l = mid + 1

    print(r)



