# RTE

import sys

input = sys.stdin.readline

n = int(input())
sx, sy, tx, ty = map(int, input().split())
circles = [list(map(int, input().split())) for _ in range(n)]
groups = {i:[] for i in range(n)}

for i in range(n):
    for j in range(i + 1, n):
        dist = (circles[i][0] - circles[j][0]) ** 2 + (circles[i][1] - circles[j][1]) ** 2
        if (dist > (circles[i][2] + circles[j][2]) ** 2) or (dist < (circles[i][2] - circles[j][2]) ** 2):
            continue
        groups[i].append(j)
        groups[j].append(i)


sidx = -1
tidx = -1
for i in range(n):
    if sidx == -1 and (((circles[i][0] - sx)**2 + (circles[i][1] - sy)**2) == circles[i][2]**2):
        sidx = i
    if tidx == -1 and (((circles[i][0] - tx)**2 + (circles[i][1] - ty)**2) == circles[i][2]**2):
        tidx = i

visited = [False for _ in range(n)]
def dfs(now):
    visited[now] = True
    if now == tidx:
        return True
    for i in groups[now]:
        if visited[i]:
            continue
        if dfs(i):
            return True

    return False


ans = dfs(sidx)
print("Yes" if ans else "No")