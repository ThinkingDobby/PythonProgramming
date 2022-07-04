# WA

import math
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

homes = []
chicks = []

for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            homes.append([i, j])
        elif data[i][j] == 2:
            chicks.append([i, j])

memo = [[i, 0] for i in range(len(chicks))]
for i in range(len(chicks)):
    for j in homes:
        memo[i][1] += abs(chicks[i][0] - j[0]) + abs(chicks[i][1] - j[1])

lim = list(map(lambda x: x[0], sorted(memo, key=lambda x: x[1])[:m]))

cnt = 0
for i in homes:
    mv = math.inf
    for j in lim:
        tmp = abs(chicks[j][0] - i[0]) + abs(chicks[j][1] - i[1])
        mv = min(mv, tmp)
    cnt += mv

print(memo)
print(lim)

print(cnt)