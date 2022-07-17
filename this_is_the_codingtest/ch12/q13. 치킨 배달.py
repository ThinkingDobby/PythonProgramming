import itertools
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

chick_for_each_homes = []
for i in homes:
    tmp = []
    for j in range(len(chicks)):
        tmp.append([j, abs(i[0] - chicks[j][0]) + abs(i[1] - chicks[j][1])])
    chick_for_each_homes.append(sorted(tmp, key=lambda x: x[1]))
# print(chick_for_each_homes)

tmp = list(range(len(chicks)))
ans = list(itertools.combinations(tmp, m))

mv = math.inf
for i in ans:
    memo = [True if j in i else False for j in range(len(chicks))]
    s = 0
    for j in chick_for_each_homes:
        for k in j:
            if memo[k[0]]:
                s += k[1]
                break
    mv = min(mv, s)

print(mv)