# Python - TLE
# PyPy - MLE

import sys
from functools import lru_cache
input = sys.stdin.readline

for _ in range(int(input())):
    n, c, q = map(int, input().split())
    s = input().rstrip()
    memo = {(0, n - 1): [(0, n - 1)]}

    @lru_cache()
    def f_idx(i, idx):
        cnt = 0
        for now in range(len(memo[i])):
            cnt += memo[i][now][1] - memo[i][now][0] + 1
            if idx < cnt:
                return (now, cnt - (memo[i][now][1] - memo[i][now][0] + 1) + idx)


    now = n
    for _ in range(c):
        l, r = map(int, input().split())
        l -= 1
        r -= 1

        le = r - l
        start = -1
        si = -1
        end = -1
        ei = -1
        s_idx = -1
        e_idx = -1

        for t in range(len(memo.keys())):
            i = list(memo.keys())[t]
            if i[0] <= l <= i[1]:
                idx = l - i[0]
                start = f_idx(i, idx)
                si = i
                s_idx = t
            if i[0] <= r <= i[1]:
                idx = r - i[0]
                end = f_idx(i, idx)
                ei = i
                e_idx = t
            if start != -1 and end != -1:
                break

        if si == ei:
            memo[(now, now + le)] = [(start[1], end[1])]
        else:
            memo[(now, now + le)] = [(memo[si][start[0]][0] + start[1], memo[si][start[0]][1])]
            memo[(now, now + le)] += memo[si][start[0] + 1:]
            for i in range(s_idx + 1, e_idx):
                memo[(now, now + le)] += memo[list(memo.keys())[i]]
            memo[(now, now + le)] += memo[ei][:end[0]]
            memo[(now, now + le)] += [(memo[ei][end[0]][0], memo[ei][end[0]][0] + end[1])]

        now += (le + 1)

    for _ in range(q):
        data = int(input()) - 1
        for i in memo.keys():
            if i[0] <= data <= i[1]:
                idx = data - i[0]
                tmp = f_idx(i, idx)
                tmp2 = tmp[1] + memo[i][tmp[0]][0]
                # print(i, tmp, tmp2)
                print(s[tmp2])

    # print(memo)
