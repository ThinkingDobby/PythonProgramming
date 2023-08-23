import collections
import math

ways = [[0, 1], [0, -1], [-1, 0], [1, 0]]


def solution(maps):
    w = len(maps[0])
    h = len(maps)

    for i in range(h):
        maps[i] = list(maps[i])

    start = [-1, -1]
    end = [-1, -1]
    lev = [-1, -1]

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'S':
                start = [i, j]
            if maps[i][j] == 'E':
                end = [i, j]
            if maps[i][j] == 'L':
                lev = [i, j]

    dq_lev = collections.deque()
    dq_lev.append(start)

    memo_lev = [[math.inf] * w for _ in range(h)]
    memo_lev[start[0]][start[1]] = 0

    while dq_lev:
        i, j = dq_lev.popleft()
        for x, y in ways:
            if 0 <= i + y < h and 0 <= j + x < w and maps[i + y][j + x] != 'X' and memo_lev[i + y][j + x] == math.inf:
                dq_lev.append([i + y, j + x])
                memo_lev[i + y][j + x] = min(memo_lev[i + y][j + x], memo_lev[i][j] + 1)

    if memo_lev[lev[0]][lev[1]] == math.inf:
        return -1
    else:
        memo_end = [[math.inf] * w for _ in range(h)]
        memo_end[lev[0]][lev[1]] = 0

        dq_end = collections.deque()
        dq_end.append(lev)

        while dq_end:
            i, j = dq_end.popleft()
            for x, y in ways:
                if 0 <= i + y < h and 0 <= j + x < w and maps[i + y][j + x] != 'X' and memo_end[i + y][j + x] == math.inf:
                    dq_end.append([i + y, j + x])
                    memo_end[i + y][j + x] = min(memo_end[i + y][j + x], memo_end[i][j] + 1)

        if memo_end[end[0]][end[1]] == math.inf:
            return -1
        else:
            return memo_lev[lev[0]][lev[1]] + memo_end[end[0]][end[1]]


print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))