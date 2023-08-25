import collections
import math

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def solution(maps):
    w = len(maps[0])
    h = len(maps)

    memo = [[math.inf] * w for _ in range(h)]
    memo[0][0] = 1

    dq = collections.deque()
    dq.append([0, 0])

    while dq:
        y, x = dq.popleft()

        for a, b in directions:
            if 0 <= y + a < h and 0 <= x + b < w and memo[y + a][x + b] == math.inf and maps[y + a][x + b] == 1:
                dq.append([y + a, x + b])
                memo[y + a][x + b] = memo[y][x] + 1

    return -1 if memo[h - 1][w - 1] == math.inf else memo[h - 1][w - 1]


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))