# TLE

import sys

input = sys.stdin.readline

n, q, x = map(int, input().split())
w = list(map(int, input().split()))

ans = []
tmp = []
s = 0
idx = 0
lim = -1
while True:
    i = w[idx]
    s += i
    tmp.append(i)
    if s >= x:
        s = 0
        if tmp in ans:
            lim = ans.index(tmp)
            break
        ans.append(tmp)
        tmp = []
    idx += 1
    if idx >= n:
        idx = 0

lens = [len(i) for i in ans]
l = len(ans)
for i in range(q):
    k = int(input())
    if k - 1 >= l:
        tmp = l - lim
        print(lens[lim + ((k - 1 - l) % tmp)])
    else:
        print(lens[k - 1])