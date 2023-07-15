# RTE

import sys

sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline
mod = 10**9 + 7

n, p = map(int, input().split())
data = list(map(int, input().split()))
tmp = 2**p

from functools import lru_cache


cnt = 0
@lru_cache()
def func(n):
    global cnt
    if n < tmp:
        cnt = (cnt + 1) % mod
        func(2 * n + 1)
        func(4 * n)
    else:
        return


for i in data:
    func(i)
print(cnt)