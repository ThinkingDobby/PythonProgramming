import collections
import copy
import itertools
import math
import sys

input = sys.stdin.readline


def bfs(start, chk):
    dq = collections.deque()
    dq.append(start)
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    cnt = 0
    while dq:
        nx, ny = dq.popleft()
        for x, y in move:
            if 0 <= nx + x < n and 0 <= ny + y < m and chk[nx + x][ny + y] == 0:
                dq.append([nx + x, ny + y])
                chk[nx + x][ny + y] = -1
                cnt += 1

    return cnt


n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

zeros = []
virus = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            zeros.append([i, j])
        elif data[i][j] == 2:
            virus.append([i, j])

cases = list(itertools.combinations(zeros, 3))
min_v = math.inf
for case in cases:
    tmp = copy.deepcopy(data)
    for i, j in case:
        tmp[i][j] = 1

    cnt = 0
    for i in virus:
        cnt += bfs(i, tmp)
    min_v = min(min_v, cnt)

print(len(zeros) - 3 - min_v)