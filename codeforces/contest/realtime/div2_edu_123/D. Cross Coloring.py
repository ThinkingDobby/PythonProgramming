# wa

import sys

input = sys.stdin.readline

mod = 998244353

for _ in range(int(input())):
    n, m, k, q = map(int, input().split())

    rows = [0] * n
    cols = [0] * m

    for i in range(1, q + 1):
        x, y = map(int, input().split())
        rows[x - 1] = i
        cols[y - 1] = i
        if all(rows):
            cols = [0] * m
        elif all(cols):
            rows = [0] * n

    tmp = set(rows + cols)
    cnt = len(tmp)
    ans = 1
    if 0 in tmp:
        cnt -= 1
    while cnt:
        ans = (ans * k) % mod
        cnt -= 1
    print(ans)
