# RTE

import sys

input = sys.stdin.readline

n = int(input())
sx, sy, tx, ty = map(int, input().split())
circles = [list(map(int, input().split())) for _ in range(n)]

sidx = -1
tidx = -1
for i in range(n):
    if sidx == -1 and (((circles[i][0] - sx)**2 + (circles[i][1] - sy)**2) == circles[i][2]**2):
        sidx = i
    if tidx == -1 and (((circles[i][0] - tx)**2 + (circles[i][1] - ty)**2) == circles[i][2]**2):
        tidx = i


def dfs(v, now):
    v[now] = True
    if now == tidx:
        return True
    for i in range(n):
        if v[i]:
            continue
        dist = (circles[i][0] - circles[now][0])**2 + (circles[i][1] - circles[now][1])**2
        if dist > (circles[i][2] + circles[now][2])**2 or dist < (circles[i][2] - circles[now][2])**2:
            continue

        if dfs(v, i):
            return True

    return False


visited = [False for _ in range(n)]
ans = dfs(visited, sidx)
print("Yes" if ans else "No")
